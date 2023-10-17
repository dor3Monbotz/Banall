import os
from os import getenv

class Config:
    TELEGRAM_TOKEN = getenv("TELEGRAM_TOKEN", "6295293651:AAFlc75675ggVEsqcyDwLAddRCIneHQRI_M")
    PYRO_SESSION = getenv("PYRO_SESSION", "BQBJFlM99XjIbWHweYQV_xEB_3HH7fkV89mu7cSSMDwZ-OWrT8MNIW-bgpPczSXAaq6JC7_qq4Y8OR2Hp8L3EmqX4mWLl7yKlY2patEyw4VYjb9tqlCBSDl6mrHYoPSM6cBMBvnqxVUG5xsNv2jn6BeniHHyD1F1zDy9qQiJ3t1itn2PBa0ClCD9B72av2yZt6D68Cg4yRubUeladkvqw8qeK0c4s3K5Pd0A0xMf6tK-UzHowZ-6VcNqeyHzJLbci9Ndlpm_qF2zheXemdOWr02spUMdntRtwR0aM2UCzBD1raU0Lvt7A9FmejZItx8NaNsfPM8FhdgMDCThq1whG5dVAAAAAXd1EakA")
    TELEGRAM_APP_HASH= getenv('TELEGRAM_APP_HASH', "2b445de78e5baf012a0793e60bd4fbf5")
    TELEGRAM_APP_ID=int(getenv('TELEGRAM_APP_ID', "19099900"))
        
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
    if not TELEGRAM_TOKEN or not PYRO_SESSION:
        raise ValueError("PYRO_SESSION / TELEGRAM_TOKEN not set")
