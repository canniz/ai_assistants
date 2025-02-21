tools = [{
        "type": "function",
        "function": {
            "name": "get_emails",
            "description": "Get user unread emails",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
                "additionalProperties": False
            },
            "strict": True
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_calendar_events",
            "description": "Recupera eventi nel calendario nell'intervallo definito dai parametri.",
            "parameters": {
                "type": "object",
                "properties": {
                    "start_date_time": {
                        "type": "string",
                        "description": "Start date-time in ISO8601 format. Utilizza sempre UTC+1"
                    },
                    "end_date_time": {
                        "type": "string",
                        "description": "End date-time in ISO8601 format. Utilizza sempre UTC+1"
                    }
                },
                "required": [
                    "start_date_time", "end_date_time"
                ],
                "additionalProperties": False
            },
            "strict": True
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_event",
            "description": "Crea un evento nel calendario, da usare quando l'utente chiede di segnare in agenda o di ricordare cose.",
            "parameters": {
                "type": "object",
                "properties": {
                    "start_date_time": {
                        "type": "string",
                        "description": "Start date-time in ISO8601 format. Utilizza sempre UTC+1"
                    },
                    "end_date_time": {
                        "type": "string",
                        "description": "End date-time in ISO8601 format. Utilizza sempre UTC+1"
                    },
                    "summary": {
                        "type": "string",
                        "description": "Titolo dell'evento"
                    }
                },
                "required": [
                    "start_date_time", "end_date_time", "summary"
                ],
                "additionalProperties": False
            },
            "strict": True
        }
    },{
        "type": "function",
        "function": {
            "name": "delete_and_update_temporary_memory",
            "description": """Aggiorna la memoria temporanea utilizzata per attività, promemoria e note temporanee.
                Questa funzione sostituisce l'intero contenuto della memoria temporanea.
                Da utilizzare per gestire contenuti dinamici come:
                - Liste di cose da fare
                - Liste della spesa
                - Promemoria temporanei
                - Note che non necessitano di essere permanenti
                Il contenuto deve essere strutturato con ritorni a capo (\\n) per maggiore leggibilità.""",
            "parameters": {
                "type": "object",
                "properties": {
                    "new_memory": {
                        "type": "string",
                        "description": "Il nuovo contenuto che sostituirà quello esistente nella memoria temporanea. Usa ritorni a capo (\\n) per strutturare il contenuto."
                    }
                },
                "required": ["new_memory"],
                "additionalProperties": False
            },
            "strict": True
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_temporary_memory",
            "description": """Recupera il contenuto attuale della memoria temporanea.
                Utilizzalo per controllare le liste delle cose da fare, i promemoria e le note temporanee.""",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
                "additionalProperties": False
            },
            "strict": True
        }
    },
    {
        "type": "function",
        "function": {
            "name": "append_string_to_permanent_memory",
            "description": """Aggiunge nuove informazioni alla memoria permanente dell'utente.
                Da utilizzare per memorizzare informazioni persistenti sull'utente come:
                - Preferenze e impostazioni
                - Fatti importanti sull'utente
                - Obiettivi a lungo termine
                - Abitudini o pattern ricorrenti
                - Informazioni personali da mantenere nel tempo
                NON utilizzare per note temporanee o promemoria.
                Il contenuto viene automaticamente aggiunto con un ritorno a capo (\\n).""",
            "parameters": {
                "type": "object",
                "properties": {
                    "string_to_append": {
                        "type": "string",
                        "description": "La nuova informazione da aggiungere alla memoria permanente. Verrà automaticamente aggiunto un ritorno a capo all'inizio."
                    }
                },
                "required": ["string_to_append"],
                "additionalProperties": False
            },
            "strict": True
        }
    }
]