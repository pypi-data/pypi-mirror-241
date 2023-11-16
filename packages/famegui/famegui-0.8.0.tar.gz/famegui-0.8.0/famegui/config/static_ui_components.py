from famegui.agent_controller import AgentController


def build_new_contract_dlg(sender: AgentController, receiver: AgentController) -> str:
    return f"""<html><head/><body>
    <p>Create new contract between:</p>
    <ul>
    <li>Sender: agent <b>{sender.display_id}</b> of type <b>{sender.type_name}</b></li>
    <li>Receiver: agent <b>{receiver.display_id}</b> of type <b>{receiver.type_name}</b></li>
    </ul>
    </body></html>
    """



