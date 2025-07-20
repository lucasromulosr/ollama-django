from django.contrib.sessions.backends.db import SessionStore


MESSAGE_HISTORY = 'message_history'


def get_message_history(session: SessionStore) -> list[dict]:
    if MESSAGE_HISTORY not in session:
        session[MESSAGE_HISTORY] = []
        session.save()
    return session.get(MESSAGE_HISTORY)


def append_message_history(session: SessionStore, role: str, content: str):
    message_history = get_message_history(session)
    message_history.append({
        'role': role, 'content': content
    })
    session.save()
