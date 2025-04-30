# def diagnose(symptoms):
#     symptoms = [s.strip().lower() for s in symptoms]

#     if (s in symptoms for s in ["fever", "cough", "fatigue"]):
#         return "You may have the flu."
#     elif all(s in symptoms for s in ["fever", "headache", "stiff neck"]):
#         return "You may have meningitis. Please consult a doctor immediately."
#     elif all(s in symptoms for s in ["sneezing", "runny nose", "sore throat"]):
#         return "You may have a common cold."
#     elif all(s in symptoms for s in ["chest pain", "shortness of breath"]):
#         return "You may have a heart problem. Seek medical attention immediately."
#     elif all(s in symptoms for s in ["abdominal pain", "diarrhea"]):
#         return "You may have a stomach infection."
#     elif all(s in symptoms for s in ["itchy eyes", "sneezing", "runny nose"]):
#         return "You may be experiencing an allergic reaction."
#     else:
#         return "Diagnosis not found. Please consult a healthcare professional."

# def main():
#     print("Welcome to the Medical Diagnosis System.")
#     user_input = input("Enter symptoms (comma-separated): ")
#     symptoms = [s.strip() for s in user_input.split(",") if s.strip()]

#     if symptoms:
#         print("\nDiagnosis:", diagnose(symptoms))
#     else:
#         print("No symptoms entered. Unable to diagnose.")

# if __name__ == "__main__":
#     main()


def diagnose():
    print("Welcome to the Medical Diagnosis Expert System.")
    symptoms_input = input("Enter symptoms: ").strip().lower()

    def has(symptom_list):
        return any(symptom in symptoms_input for symptom in symptom_list)

    if has(["fever", "cough", "fatigue"]):
        print( "You may have the flu.")

    elif has(["sneezing", "runny nose", "sore throat"]):
        print ( "You may have a common cold.")

    elif has(["chest pain", "shortness of breath"]):
        print ("You may have a heart problem. Seek medical attention immediately.")

    elif has(["abdominal pain", "diarrhea"]):
        print( "You may have a stomach infection.")

    elif has(["rash", "itchy eyes"]):
        print( "You may be experiencing an allergic reaction.")

    else:
        print( "Diagnosis not found. Please consult a healthcare professional.")


diagnose()
