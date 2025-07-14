import logging
import azure.functions as func
import pandas as pd
import io

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        file = req.files.get('file')
        if not file:
            return func.HttpResponse("No file uploaded", status_code=400)

        contents = file.read()
        df = pd.read_csv(io.BytesIO(contents))

        if 'EmployeeID' not in df.columns or 'Name' not in df.columns:
            return func.HttpResponse("Invalid CSV: Missing EmployeeID or Name", status_code=400)

        return func.HttpResponse("Validation Passed", status_code=200)

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return func.HttpResponse("Something went wrong", status_code=500)
