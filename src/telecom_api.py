from fastapi import FastAPI
import pandas as pd
import numpy as np

app = FastAPI()

@app.get("/new_customers")
def get_new_customers():

    n = 200
    np.random.seed(100)

    data = pd.DataFrame({
        "customer_id": range(2001, 2001+n),
        "gender": np.random.choice(["Male","Female"], n),
        "senior_citizen": np.random.choice([0,1], n, p=[0.85,0.15]),
        "tenure_months": np.random.randint(1, 24, n),
        "monthly_charges": np.random.uniform(30, 130, n).round(2),
        "contract_type": np.random.choice(["Month-to-month","One year","Two year"], n),
        "internet_service": np.random.choice(["DSL","Fiber optic","No"], n),
        "online_security": np.random.choice([0,1], n),
        "tech_support": np.random.choice([0,1], n),
        "payment_method": np.random.choice(
            ["Electronic check","Mailed check","Bank transfer","Credit card"],
            n
        ),
        "support_calls": np.random.randint(0,6,n)
    })

    data["total_charges"] = (data["monthly_charges"] * data["tenure_months"]).round(2)

    # churn probability
    data["churn"] = np.where(
        (data["contract_type"]=="Month-to-month") &
        (data["support_calls"]>3),
        1,
        0
    )

    return data.to_dict(orient="records")
