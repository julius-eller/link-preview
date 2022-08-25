def find_cookie_match(button_text):
    cookie_shorthand_matches = [
        ["Accept", "Agree", "Allow", "Approve", "Continue", "Got it", "I agree", "I accept", "I understand", "OK", "Okay", "Save preferences", "Save settings", "Save", "Set preferences", "Set settings", "Set", "Sure", "Yes"],
        ["Alle", "Akzeptieren", "Annehmen", "Einverstanden", "Einwilligen", "stimme zu", "akzeptiere", "verstehe", "OK", "Okay", "Einstellungen speichern", "Speichern", "Sicher", "Ja", "Zustimmen", "Fortfahren"],
        ["Accetto", "Acconsento", "Continua", "Ho capito", "OK", "Okay", "Salva le preferenze", "Salva le impostazioni", "Salva", "Impostazioni salvate", "Impostazioni", "Imposta le preferenze", "Imposta le impostazioni", "Imposta", "Sicuro", "Si"],
        ["Aceptar", "Acepto", "Aprobar", "Continuar", "Entiendo", "OK", "Okay", "Guardar preferencias", "Guardar configuración", "Guardar", "Preferencias guardadas", "Configuración guardada", "Configuración", "Establecer preferencias", "Establecer configuración", "Establecer", "Seguro", "Sí"],
        ["Accepter", "J'accepte", "J'ai compris", "OK", "Okay", "Enregistrer les préférences", "Enregistrer les paramètres", "Enregistrer", "Préférences enregistrées", "Paramètres enregistrés", "Paramètres", "Définir les préférences", "Définir les paramètres", "Définir", "Sûr", "Oui"],
        ["Accepteren", "Akkoord", "Begrijp ik", "Doorgaan", "Ga verder", "Ik ga akkoord", "Ik ga ermee akkoord", "Ik ga ermee in", "OK", "Okay", "Voorkeuren opslaan", "Instellingen opslaan", "Opslaan", "Instellingen opgeslagen", "Instellingen", "Voorkeuren instellen", "Instellingen instellen", "Instellen", "Zeker", "Ja"],
        ["Aceitar", "Aceito", "Aprovar", "Continuar", "Entendi", "OK", "Okay", "Salvar preferências", "Salvar configurações", "Salvar", "Preferências salvas", "Configurações salvas", "Configurações", "Definir preferências", "Definir configurações", "Definir", "Certo", "Sim"]
    ]
    # Check if a part of the text matches shorthand matches:
    for cookie_list in cookie_shorthand_matches:
        for cookie_shorthand in cookie_list:
            if cookie_shorthand.lower() in button_text.lower():
                return True
    return False