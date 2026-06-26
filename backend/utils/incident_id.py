from datetime import datetime
import uuid


def generate_incident_id():

    today = datetime.utcnow().strftime("%Y%m%d")

    short = str(uuid.uuid4())[:6].upper()

    return f"INC-{today}-{short}"
