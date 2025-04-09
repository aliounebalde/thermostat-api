# app/config.py

COLD_TOLERANCE = 0.3
HOT_TOLERANCE = 0.3
MIN_CYCLE_DURATION = 300  # secondes
DEFAULT_TARGET_TEMP = 22.0
MQTT_BROKER_URL = "localhost"
MQTT_TOPIC_UP = "sensor/temp"
MQTT_TOPIC_DOWN = "actuator/heater/set"
