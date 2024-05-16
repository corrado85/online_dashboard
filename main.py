import datetime

def generate_monthly_report():
    # Codice per generare il report mensile
    report = f"Report del mese: {datetime.datetime.now().strftime('%B %Y')}\n"
    report += "Dati e statistiche...\n"
    return report

if __name__ == "__main__":
    report = generate_monthly_report()
    with open("report.txt", "w") as file:
        file.write(report)
