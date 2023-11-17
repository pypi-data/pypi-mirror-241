from datetime import datetime
import tensorflow as tf
import numpy as np
import cv2

import comun_sqlsrv
import comun_mail


class AILog:
    def __init__(self, endpoint_name: str, endpoint_data_received: str):
        self.date_time = datetime.now()
        self.endpoint_name = endpoint_name
        self.endpoint_data_received = endpoint_data_received
        self.result = "KO_199"
        self.prediction = None
        self.img_path = None
        self.img_name = None
        self.img_frame = None
        self.error = None
        self.bar_code = None

    def __str__(self):
        return f"""
                LOG:
                Date: {self.date_time},
                Endpoint name: {self.endpoint_name},
                Endpoint received data: {self.endpoint_data_received},
                Result: {self.result},
                Prediction: {self.prediction}         
                """

    def save_log(self, mssql_srv: str, database: str, user: str, passwd: str, rescale_size: tuple = None):
        """
        Save the image in local path and the data into the DB
        :param mssql_srv: IP of the MSSQL server
        :param database: Name of the database
        :param user: User of the database
        :param passwd: Password of the user
        :param rescale_size: A tuple with the HxW (in px) to rescale the image, example: (500, 500)
        :return: doesn't return anything
        """
        # SAVE IMAGE:
        if self.img_frame is not None:
            if self.img_name is None:
                self.img_name = f'{self.date_time.strftime("%Y_%m_%d_%H_%M_%S")}.jpg'
            if self.img_path is None:
                self.img_path = f'img_save/{self.img_name}'
            if rescale_size:
                self.img_frame = cv2.resize(self.img_frame, rescale_size)
            cv2.imwrite(self.img_path, self.img_frame)

        # SAVE LOG IN DB:
        mssql = comun_sqlsrv.Sql(mssql_srv, database, user, passwd)
        query = f"""
                INSERT INTO T_VA_API_LOG
                (FECHA_HORA, ENDPOINT, RESULTADO, DATO_RECIBIDO, PREDICCION_VA, NOMBRE_IMAGEN, COD_BAR, ERROR)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                """
        query_values = (self.date_time,
                        self.endpoint_name,
                        self.result,
                        self.endpoint_data_received,
                        self.prediction,
                        self.img_name,
                        self.bar_code,
                        self.error)
        mssql.ejecutar(query, query_values)
        mssql.cerrar_conexion()

    def send_email_info(self, smtp_host: str, email_subject: str, receiver: list):
        """
        Send an email with VA information
        :param smtp_host: IP and port of the smtp server, example: "10.10.10.5:587"
        :param email_subject: String with the subject of the email
        :param receiver: list with email destinations, example: ["miki@gmail.es","adolfo@gmail.es"]
        :return: doesn't return anything
        """
        msg = f"""
                INFORME VISIÓN:
                
                Nombre del endpoint (URL llamada): {self.endpoint_name} \n
                Datos recibidos por el endpoint: {self.endpoint_data_received} \n
                Resultado (respuesta a la llamada): {self.result} \n            
                """
        if self.prediction is not None:
            msg += f"""Predicción de la vision: {self.prediction} \n"""
        if self.img_path is not None:
            comun_mail.send_mail(smtp_host, msg, email_subject, receiver, self.img_path)
        else:
            comun_mail.send_mail(smtp_host, msg, email_subject, receiver)


def get_image_from_ip_camera(camera_url: str, frames_to_calibrate: int = 1):
    """
    Function that connect to an IP camera and return a frame
    :param camera_url: need to be the RTSP URL
    :param frames_to_calibrate: Sometimes the iris of the camera needs some frames to calibrate, otherwise the
    image cud be too brightness or too dark
    :return: given frame from OpenCV when you read a video capture
    """
    try:
        cap = cv2.VideoCapture(camera_url)  # IP Camera
        for _ in range(frames_to_calibrate):
            success, frame = cap.read()
            if not success:
                raise Exception
        cap.release()
        return frame

    except Exception:
        raise Exception(f"No se ha podido conectar a la camara IP")


def run_model_with_frame(img_frame, class_names: dict, model_path: str, output=False, limit_gpu=False,
                         rescaled_size=(224, 224)) -> str:
    """
    Function that execute an IA model
    :param img_frame: given frame from OpenCV when you read a video capture
    :param class_names: the posibles results of the IA
    :param model_path: path from the saved model
    :param output: set to True if you want to see all predictions
    :param limit_gpu: set the GPU memory usage only to what is needed
    :param rescaled_size: the size of the images which the model has been trained (img_height, img_width)
    :return: the maximum value predicted by the model from class_names dictionary
    """
    try:
        if limit_gpu:
            # Limit the GPU memory usage only to what is needed, without this TensorFlow would use all the GPU memory.
            gpus = tf.config.experimental.list_physical_devices('GPU')
            if gpus:
                try:
                    for gpu in gpus:
                        tf.config.experimental.set_memory_growth(gpu, True)
                except RuntimeError as e:
                    print(e)

        # Disable scientific notation for clarity
        np.set_printoptions(suppress=True)

        # Load the model. Compile is not needed while prediction, only while training.
        model = tf.keras.models.load_model(model_path, compile=False)

        image_resized = cv2.resize(img_frame, rescaled_size)
        image = np.expand_dims(image_resized, axis=0)
        predictions = model.predict(image)
        index = np.argmax(predictions)
        class_name = class_names[index]

        if output:
            print("\nPREDICTION:", flush=True)
            print(f"Class name: {class_name}  Match Score: {predictions[0][index]}", flush=True)
            print(f"All predictions: {predictions}", flush=True)

        return class_name

    except Exception:
        raise Exception(f"No se ha podido ejecutar la red neuronal")
