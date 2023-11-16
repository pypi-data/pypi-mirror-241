import json
import queue
import sys
import threading
import time

import pandas as pd
import streamlit as st
import websocket
from streamlit.runtime import Runtime
from streamlit.runtime.app_session import AppSession
from streamlit.runtime.scriptrunner import add_script_run_ctx, get_script_run_ctx
from streamlit.web import cli as stcli

from besser.bot.platforms.payload import Payload, PayloadAction, PayloadEncoder

# Time interval to check if a streamlit session is still active, in seconds
SESSION_MONITORING_INTERVAL = 10


def get_streamlit_session() -> AppSession or None:
    session_id = get_script_run_ctx().session_id
    runtime: Runtime = Runtime.instance()
    return next((
        s.session
        for s in runtime._session_mgr.list_sessions()
        if s.session.id == session_id
    ), None)


def session_monitoring(interval: int):
    runtime: Runtime = Runtime.instance()
    session = get_streamlit_session()
    while True:
        time.sleep(interval)
        if not runtime.is_active_session(session.id):
            runtime.close_session(session.id)
            session.session_state['websocket'].close()
            break


def main():

    def on_message(ws, payload_str):
        # https://github.com/streamlit/streamlit/issues/2838
        streamlit_session = get_streamlit_session()
        payload: Payload = Payload.decode(payload_str)
        if payload.action == PayloadAction.BOT_REPLY_STR.value:
            message = payload.message
        elif payload.action == PayloadAction.BOT_REPLY_DF.value:
            message = pd.read_json(payload.message)
        elif payload.action == PayloadAction.BOT_REPLY_OPTIONS.value:
            d = json.loads(payload.message)
            message = []
            for button in d.values():
                message.append(button)
        streamlit_session._session_state['queue'].put(message)
        streamlit_session._handle_rerun_script_request()

    def on_error(ws, error):
        pass

    def on_open(ws):
        pass

    def on_close(ws, close_status_code, close_msg):
        pass

    def on_ping(ws, data):
        pass

    def on_pong(ws, data):
        pass

    st.set_page_config(
        page_title="Streamlit Chat - Demo",
        page_icon=":robot:"
    )

    user_type = {
        0: 'assistant',
        1: 'user'
    }

    st.header("Chat Demo")
    st.markdown("[Github](https://github.com/BESSER-PEARL/bot-framework)")

    if 'history' not in st.session_state:
        st.session_state['history'] = []

    if 'queue' not in st.session_state:
        st.session_state['queue'] = queue.Queue()

    if 'websocket' not in st.session_state:
        ws = websocket.WebSocketApp("ws://localhost:8765/",
                                    on_open=on_open,
                                    on_message=on_message,
                                    on_error=on_error,
                                    on_close=on_close,
                                    on_ping=on_ping,
                                    on_pong=on_pong)
        websocket_thread = threading.Thread(target=ws.run_forever)
        add_script_run_ctx(websocket_thread)
        websocket_thread.start()
        st.session_state['websocket'] = ws

    if 'session_monitoring' not in st.session_state:
        session_monitoring_thread = threading.Thread(target=session_monitoring,
                                                     kwargs={'interval': SESSION_MONITORING_INTERVAL})
        add_script_run_ctx(session_monitoring_thread)
        session_monitoring_thread.start()
        st.session_state['session_monitoring'] = session_monitoring_thread

    ws = st.session_state['websocket']

    with st.sidebar:
        reset_button = st.button(label="Reset bot")
        if reset_button:
            st.session_state['history'] = []
            st.session_state['queue'] = queue.Queue()
            payload = Payload(action=PayloadAction.RESET)
            ws.send(json.dumps(payload, cls=PayloadEncoder))

    for message in st.session_state['history']:
        with st.chat_message(user_type[message[1]]):
            st.write(message[0])

    first_message = True
    while not st.session_state['queue'].empty():
        message = st.session_state['queue'].get()
        t = len(message) / 1000 * 3
        if t > 3:
            t = 3
        elif t < 1 and first_message:
            t = 1
        first_message = False
        if isinstance(message, list):
            st.session_state['buttons'] = message
        else:
            st.session_state['history'].append((message, 0))
            with st.chat_message("assistant"):
                with st.spinner(''):
                    time.sleep(t)
                st.write(message)

    if 'buttons' in st.session_state:
        buttons = st.session_state['buttons']
        cols = st.columns(1)
        for i, option in enumerate(buttons):
            if cols[0].button(option):
                with st.chat_message("user"):
                    st.write(option)
                st.session_state.history.append((option, 1))
                payload = Payload(action=PayloadAction.USER_MESSAGE,
                                  message=option)
                ws.send(json.dumps(payload, cls=PayloadEncoder))
                del st.session_state['buttons']
                break

    # React to user input
    if user_input := st.chat_input("What is up?"):
        if 'buttons' in st.session_state:
            del st.session_state['buttons']
        with st.chat_message("user"):
            st.write(user_input)
        st.session_state.history.append((user_input, 1))
        payload = Payload(action=PayloadAction.USER_MESSAGE,
                          message=user_input)
        try:
            ws.send(json.dumps(payload, cls=PayloadEncoder))
        except Exception as e:
            st.error('Your message could not be sent. The connection is already closed')

    st.stop()


if __name__ == "__main__":
    if st.runtime.exists():
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
