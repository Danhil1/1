import time
import uuid
import random
from os import environ
from kafka import KafkaProducer
from src.data_model import PredictionRow
from src.constants import MAIN_KAFKA_TOPIC
from dotenv import load_dotenv

load_dotenv()

SERVER = environ.get("KAFKA_SERVERS")

producer = KafkaProducer(bootstrap_servers=SERVER)

while True:
    possible_Mean_of_the_integrated_profile = random.uniform(5.81, 190) 
    possible_Standard_deviation_of_the_integrated_profile = random.uniform(24.8, 91.8)
    possible_Excess_kurtosis_of_the_integrated_profile = random.uniform(-1.79,8.07)
    possible_Skewness_of_the_integrated_profile = random.uniform(-1.79, 68.1)
    possible_Mean_of_the_DM_SNR_curve = random.uniform(0.21, 222)
    possible_Standard_deviation_of_the_DM_SNR_curve = random.uniform(7.37, 111) 
    possible_Excess_kurtosis_of_the_DM_SNR_curve = random.uniform(-3.14, 34.5)
    possible_Skewness_of_the_DM_SNR_curve = random.uniform(-1.98, 1.19)
    pred_row = PredictionRow(Mean_of_the_integrated_profile=possible_Mean_of_the_integrated_profile, 
                                      Standard_deviation_of_the_integrated_profile=possible_Standard_deviation_of_the_integrated_profile, 
                                      Excess_kurtosis_of_the_integrated_profile=possible_Excess_kurtosis_of_the_integrated_profile,
                                        Skewness_of_the_integrated_profile=possible_Skewness_of_the_integrated_profile,
                                        Mean_of_the_DM_SNR_curve=possible_Mean_of_the_DM_SNR_curve,
                                        Standard_deviation_of_the_DM_SNR_curve=possible_Standard_deviation_of_the_DM_SNR_curve,
                                        Excess_kurtosis_of_the_DM_SNR_curve=possible_Excess_kurtosis_of_the_DM_SNR_curve,
                                        Skewness_of_the_DM_SNR_curve=possible_Skewness_of_the_DM_SNR_curve)
    
    producer.send(topic=MAIN_KAFKA_TOPIC, key=str(uuid.uuid4()).encode("utf8"), value=pred_row.json().encode("utf8"))
    time.sleep(5)
