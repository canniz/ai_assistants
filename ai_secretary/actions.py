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
}

]