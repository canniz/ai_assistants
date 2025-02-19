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
            "name": "update_memory",
            "description": """Aggiorna la memoria dell'utente. Serve per rimpiazzare il vecchio contenuto della memoria col nuovo.
                Mantieni sempre i concetti da aggiungere sintetici, non superare i 2000 caratteri. 
                La memoria dovrà contenere roba che l'utente ti chiede di ricordare, o concetti che reputi importanti da tenere a mente.
                Da usare solo se c'è da rimpiazzare o eliminare del contenuto della memoria""",
            "parameters": {
                "type": "object",
                "properties": {
                    "new_memory": {
                        "type": "string",
                        "description": """Da usare se c'è da rimpiazzare o eliminare del contenuto della memoria,
                            contiene il testo dell'intera memoria che rimpiazzerà quello vecchio"""
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
            "name": "get_memory",
            "description": """Se fosse necessario, puoi usare questa funzione per recuperare la memoria dell'utente.""",
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
            "name": "append_string_to_memory",
            "description": """Appende del contenuto alla memoria dell'utente. Serve per aggiungere contenuto senza cancellarne del vecchio.
                Mantieni sempre i concetti da aggiungere sintetici, non superare i 2000 caratteri. 
                La memoria dovrà contenere roba che l'utente ti chiede di ricordare, o concetti che reputi importanti da tenere a mente.
                Da usare solo se c'è da aggiungere contenuto alla memoria""",
            "parameters": {
                "type": "object",
                "properties": {
                    "string_to_append": {
                        "type": "string",
                        "description": """Contiene il testo da appendere alla memoria"""
                    }
                },
                "required": ["string_to_append"],
                "additionalProperties": False
            },
            "strict": True
        }
    }
]