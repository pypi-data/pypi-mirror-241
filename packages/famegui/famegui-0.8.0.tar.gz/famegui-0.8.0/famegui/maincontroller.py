import logging
import math
import typing
from PySide2 import QtCore
from fameio.source.schema import AttributeSpecs

from famegui import models
from famegui.agent_controller import AgentController
from famegui.appworkingdir import AppWorkingDir
import fameio.source.validator as fameio

from famegui.models import Agent, Contract


class ProjectProperties(QtCore.QObject):
    """Class used to attach extra properties to a scenario model and signal when they change"""

    changed = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self.reset()

    def reset(self, file_path=""):
        self._has_unsaved_changes = False
        self._file_path = file_path
        self._validation_errors = []
        self.changed.emit()

    @property
    def has_unsaved_changes(self) -> bool:
        return self._has_unsaved_changes

    def set_unsaved_changes(self, has_changes: bool = True):
        if self._has_unsaved_changes != has_changes:
            self._has_unsaved_changes = has_changes
            self.changed.emit()

    @property
    def file_path(self) -> str:
        return self._file_path

    def set_file_path(self, file_path: str) -> None:
        if self._file_path != file_path:
            self._file_path = file_path
            self.changed.emit()

    @property
    def is_validation_successful(self) -> bool:
        return len(self._validation_errors) == 0

    @property
    def validation_errors(self) -> typing.List[str]:
        return self._validation_errors

    def clear_validation_errors(self) -> None:
        was_invalid = not self.is_validation_successful
        self._validation_errors = []
        if was_invalid:
            logging.info("schema validation status changed to valid")
            self.changed.emit()

    def set_validation_error(self, msg: str) -> None:
        assert msg != ""
        was_valid = self.is_validation_successful
        self._validation_errors = [msg]
        if was_valid:
            logging.info("schema validation status changed to invalid")
            self.changed.emit()


class MainController(QtCore.QObject):
    selected_agent_changed = QtCore.Signal(AgentController)
    agent_added = QtCore.Signal(AgentController)
    contract_added = QtCore.Signal(
        AgentController, AgentController, models.Contract
    )  # sender, receiver, contract
    layout_rearranged = QtCore.Signal()
    agents_deleted = QtCore.Signal(list)
    contracts_deleted = QtCore.Signal(int)  # agent_id

    class AgentTypeBucket:
        """Class used to store information about a type of agent in the scenario.
        Used to build up orbitals in the graph view
        """

        def __init__(self, type_name: str, agent: Agent = None, agent_list=None):
            self.type_name = type_name
            self.agent_list = [agent]
            if agent_list is not None:
                self.agent_list = agent_list

        type_name: str
        degree_per_agent: float
        radius_scale_factor_per_agent_type: float
        agent_list: typing.List[Agent]
        contract_added = QtCore.Signal(
            AgentController, AgentController, models.Contract
        )  # sender, receiver, contract
        layout_rearranged = QtCore.Signal()
        agents_deleted = QtCore.Signal(list)
        contracts_deleted = QtCore.Signal(int)  # agent_id

        class AgentTypeBucket:
            """Class used to store information about a type of agent in the scenario.
            Used to build up orbitals in the graph view
            """

            def __init__(self, type_name: str, agent: Agent = None, agent_list=None):
                self.type_name = type_name
                self.agent_list = [agent]
                if agent_list is not None:
                    self.agent_list = agent_list

            type_name: str
            degree_per_agent: float
            radius_scale_factor_per_agent_type: float
            agent_list: typing.List[Agent]

    def __init__(self, working_dir: AppWorkingDir):
        super().__init__()
        logging.debug("initializing main controller")
        self._working_dir = working_dir
        self._scenario_model = None
        self._agents: typing.Dict[int, AgentController] = {}
        self._contracts = {}
        self._project_properties = ProjectProperties()

    def reset(self, scenario: models.Scenario = None) -> None:
        self._agents = {}
        self._contracts = {}
        self._scenario_model = scenario
        self._project_properties.reset()

    @property
    def is_open(self) -> bool:
        return self._scenario_model is not None

    @property
    def has_unsaved_changes(self) -> bool:
        return self.project_properties.has_unsaved_changes

    @property
    def project_properties(self) -> ProjectProperties:
        return self._project_properties

    @property
    def schema(self) -> models.Schema:
        return self.scenario.schema

    @property
    def scenario(self) -> models.Scenario:
        return self._scenario_model

    def update_scenario_properties(self, props: models.GeneralProperties):
        has_changed = self._scenario_model.update_properties(props)
        if has_changed:
            self._project_properties.set_unsaved_changes(True)

    @property
    def can_export_protobuf(self) -> bool:
        return (
                self.is_open
                and self.project_properties.is_validation_successful
                and not self.has_unsaved_changes
        )

    @property
    def agent_count(self) -> int:
        """get total agent count of scenario"""
        return len(self._agents)

    @property
    def agent_list(self) -> typing.List[AgentController]:
        return self._agents.values()

    def agent_from_id(self, id: int) -> AgentController:
        """get agent by id"""
        assert id in self._agents
        return self._agents[id]

    @property
    def contract_count(self) -> int:
        """get total contract count of scenario"""
        return len(self._contracts)

    def get_agent_ctrl(self, agent_id: int) -> AgentController:
        """get agent controller by agent id"""
        return self._agents[agent_id]

    def get_agent_type(self, agent_id: int) -> str:
        """get agent type by agent id"""
        return self._agents[agent_id].type_name

    def get_all_agents_by_type_name(self, agent_type_name: str) -> typing.List[Agent]:
        """filter to get all agents from scenario by agent type"""
        is_agent_from_agent_type = lambda agent: agent.type_name == agent_type_name
        return list(filter(is_agent_from_agent_type, self.scenario.agents))

    def _get_agent_bucket_list(self, agent_list: list) -> list:
        """create agent buckets by agent type"""
        agent_type_bucket_list = []

        for agent in agent_list:
            for x in agent_type_bucket_list:
                if x.type_name == agent.type_name:
                    x.agent_list.append(agent)
                    break
            else:
                agent_type_bucket_list.append(
                    self.AgentTypeBucket(agent.type_name, agent)
                )
        return agent_type_bucket_list

    def prepare_and_sort_agent_buckets(self, agent_type_bucket_list):
        """sort agent buckets by length of agent list"""
        new_agents_list = []
        for item in agent_type_bucket_list:
            new_agents_list.append(item.agent_list)
        new_agents_list.sort(key=len)
        return new_agents_list

    @staticmethod
    def _split_agent_types_into_chunks(agent_type_bucket_list):
        """split huge agent bucket into separate to make canvas look better
        create more buckets to make more smaller orbitals"""

        agent_types_to_re_gen_list = []
        chunked_list = []

        for item in agent_type_bucket_list:
            if len(item.agent_list) > 360:
                agent_types_to_re_gen_list.append(item.type_name)

                for i in range(0, len(item.agent_list), 360):
                    chunked_list.append(item.agent_list[i: i + 360])
        return agent_types_to_re_gen_list, chunked_list

    @staticmethod
    def _calc_degree_per_agent_in_agent_circle(agent_type_bucket_list):
        """calculate degree per agent in agent orbitale"""
        for item in agent_type_bucket_list:
            item.degree_per_agent = 360 / len(item.agent_list)

    @staticmethod
    def _update_graph_items(agent_ctrl_list, new_agent_x, new_agent_y, agent):
        """Updates the graph item coords of the agent with the supplied id"""
        for agent_ctrl in agent_ctrl_list:
            if agent.id.__eq__(agent_ctrl.id):
                agent_ctrl.scene_item.setPos(new_agent_x, new_agent_y)
                agent_ctrl.model_was_modified.emit()
                agent_ctrl.position_changed()
                break

    def get_amount_of_related_contract(self, agent_id: int):
        """Returns the amount of contracts related to the supplied agent"""
        amount_of_related_contract = 0
        for contract in self.scenario.contracts:
            if contract.sender_id == agent_id or contract.receiver_id == agent_id:
                amount_of_related_contract += 1
        return amount_of_related_contract

    def get_all_related_contracts(self, agent_id: int):
        """'Returns a list of all contracts related to the supplied agent"""
        related_contract_list = []
        for contract in self.scenario.contracts:
            if contract.sender_id == agent_id or contract.receiver_id == agent_id:
                related_contract_list.append(contract)
        return related_contract_list

    def delete_all_related_contracts(self, agent_id: int):
        """clear all related contracts of the supplied agent. emit signal to communicate with canvas"""
        self.contracts_deleted.emit(int(agent_id))
        self.scenario.del_all_related_contracts(int(agent_id))
        self._project_properties.set_unsaved_changes(True)

    def delete_all_related_contracts_from_scenario(self, agent_id: int):
        """clear all related contracts of the supplied agent"""
        self.scenario.del_all_related_contracts(agent_id)

    def remove_contract(self, sender_id: int, receiver_id: int, product_name: str):
        """remove contract from scenario"""
        for contract in self.scenario.contracts:
            if (
                    contract.sender_id == sender_id
                    and contract.receiver_id == receiver_id
                    and contract.product_name == product_name
            ):
                self.scenario.contracts.remove(contract)
            self._project_properties.set_unsaved_changes(True)

    def remove_agent(self, agent_id: int):
        """remove agent from scenario and delete all related contracts"""
        agent_id = int(agent_id)
        agents_to_delete = []
        self.agents_deleted.emit([agent_id])
        for agent in self.scenario.agents:
            if agent.id == agent_id:
                self.scenario.agents.remove(agent)
                agents_to_delete.append(agent)
                self.delete_all_related_contracts_from_scenario(agent_id)
        self.agents_deleted.emit([agent_id])

        self._project_properties.set_unsaved_changes(True)

    # New sub-function to handle agent positioning
    def _adjust_agent_position(self, item, default_radius, radius, margin, last_x, last_y):
        '''Adjusts the position of the agent in the scene by building a orbital model'''
        for i in range(0, len(item.agent_list)):
            agent = item.agent_list[i]
            degree = item.degree_per_agent * (i + 1)

            new_agent_x, new_agent_y, temp_rad = self._calculate_new_position(
                default_radius, degree, last_x, last_y, radius, margin
            )

            if not self.rearrange_mode:
                agent.set_display_xy(int(new_agent_x), int(new_agent_y))
                return new_agent_x, new_agent_y, temp_rad, [agent]

            self._adjust_agent_postions(self._agents, new_agent_x, new_agent_y, agent)

        return last_x, last_y, default_radius, []

    # Helper function to calculate new position
    def _calculate_new_position(self, default_radius, degree, last_x, last_y, radius, margin):
        """Helper function to calculate the new position of the agent"""

        new_agent_x = default_radius * math.cos(math.radians(degree))
        new_agent_y = default_radius * math.sin(math.radians(degree))

        distance = math.sqrt((new_agent_x - last_x) ** 2 + (new_agent_y - last_y) ** 2)
        temp_rad = default_radius

        if last_x != 0.0 and last_y != 0.0:
            while distance <= (radius * 2):
                temp_rad = temp_rad * 1.1
                new_agent_x = temp_rad * math.cos(math.radians(degree))
                new_agent_y = temp_rad * math.sin(math.radians(degree))
                distance = math.sqrt((new_agent_x - last_x) ** 2 + (new_agent_y - last_y) ** 2)

        return new_agent_x, new_agent_y, temp_rad

    def delete_all_related_agents(self, agent_id: int):
        """delete all agents that are directly connected through agents to the passed agent_id"""
        unique_agent_id_set = set()
        related_contract_list = self.get_all_related_contracts(agent_id)
        unique_agent_id_set.add(agent_id)
        for contract in related_contract_list:
            unique_agent_id_set.add(contract.sender_id)
            unique_agent_id_set.add(contract.receiver_id)

        for agent in self.scenario.agents:
            if agent.id in unique_agent_id_set:
                self.scenario.agents.remove(agent)
        self._has_unsaved_changes = True

    def _build_agent_type_bucket_list(self, agent_list: list, agent_type_bucket_list: list):
        """Builds a list that wraps the agent list into agent type buckets to build a agent orbitals model"""
        for sub_list in agent_list:
            agent_type_bucket_list.append(
                self.AgentTypeBucket(sub_list[0].type_name, agent_list=sub_list)
            )
        return agent_type_bucket_list

    def _prep_buckets_for_rearrange(self):
        """split huge agent bucket into separate to make canvas look better by creating orbitals"""
        agent_list: list = self.agent_list
        agent_type_bucket_list = self._get_agent_bucket_list(agent_list)

        new_list = []
        for item in self.prepare_and_sort_agent_buckets(agent_type_bucket_list):
            for x in item:
                new_list.append(x)
        agent_types_to_re_gen_list, chunked_list = self._split_agent_types_into_chunks(
            agent_type_bucket_list
        )

        for type_to_rm in agent_types_to_re_gen_list:
            agent_type_bucket_list = [
                value
                for value in agent_type_bucket_list
                if value.type_name != type_to_rm
            ]

        agent_type_bucket_list = self._build_agent_type_bucket_list(chunked_list, agent_type_bucket_list)

        self._calc_degree_per_agent_in_agent_circle(agent_type_bucket_list)

        return sorted(agent_type_bucket_list, key=lambda x: len(x.agent_list))

    def auto_scale_scenario_graph(
            self, agent_ctrl_list: [AgentController], rearrange_mode=False
    ):
        """initiate auto scale of scenario graph into orbital model"""
        try:
            # predefined zoom steps
            default_radius = 100.0
            radius = 50
            margin = 20
            last_x = 0.0
            last_y = 0.0
            min_distance = (float(radius) * 2) + float(margin)

            prep_buckets_for_rearrange = self._prep_buckets_for_rearrange()
            last_list = []

            for item in prep_buckets_for_rearrange:
                # expand rad for new circle
                new_radius = default_radius * 1.1
                if new_radius - default_radius < min_distance:
                    new_radius = new_radius + radius * 2 + margin
                default_radius = new_radius

                for i in range(0, len(item.agent_list)):
                    agent = item.agent_list[i]
                    degree = item.degree_per_agent
                    for counter in range(0, i):
                        degree = degree + item.degree_per_agent
                    new_agent_x = default_radius * math.cos(math.radians(degree))
                    new_agent_y = default_radius * math.sin(math.radians(degree))
                    distance = math.sqrt(
                        (new_agent_x - last_x) ** 2 + (new_agent_y - last_y) ** 2
                    )
                    temp_rad: float = default_radius

                    if last_x != 0.0 and last_y != 0.0:
                        # adjust till all spacing requirements are met
                        while distance <= (radius * 2):
                            temp_rad = temp_rad * 1.1
                            new_agent_x = temp_rad * math.cos(math.radians(degree))
                            new_agent_y = temp_rad * math.sin(math.radians(degree))
                            distance = math.sqrt(
                                (new_agent_x - last_x) ** 2
                                + (new_agent_y - last_y) ** 2
                            )

                    default_radius = temp_rad
                    last_x = new_agent_x
                    last_y = new_agent_y

                    if not rearrange_mode:
                        agent.set_display_xy(int(new_agent_x), int(new_agent_y))
                        last_list.append(agent)
                        continue

                    self._update_graph_items(
                        agent_ctrl_list, new_agent_x, new_agent_y, agent
                    )

            if not rearrange_mode:
                for a in last_list:
                    self._create_agent_controller(a)
                for c in self._scenario_model.contracts:
                    self._create_contract_model(c)

        except Exception as e:
            logging.error("failed to init the given scenario: {}".format(e))
            self.reset()
            raise

        # refresh the UI
        self._project_properties.changed.emit()

    def compute_scene_rect(self) -> QtCore.QRectF:
        rect = QtCore.QRectF(0, 0, 1000, 1000)

        if len(self.agent_list) >= 5000:
            rect = QtCore.QRectF(0, 0, 100000, 100000)

        for a in self.agent_list:
            margin = 20
            item_size = a.scene_item.boundingRect().width()
            left = a.scene_item.x() - margin
            right = a.scene_item.x() + item_size + margin
            top = a.scene_item.y() + -margin
            bottom = a.scene_item.y() + item_size + margin
            if left < rect.left():
                rect.setLeft(left)
            if right > rect.right():
                rect.setRight(right)
            if top < rect.top():
                rect.setTop(top)
            if bottom > rect.bottom():
                rect.setBottom(bottom)

        return rect

    def get_contract(self, sender_id, receiver_id, product_name) -> Contract:
        for i in self.scenario.contracts:
            i: Contract
            if i.product_name.__eq__(product_name):
                if i.sender_id.__eq__(sender_id) and i.receiver_id.__eq__(receiver_id):
                    return i

                elif i.sender_id.__eq__(receiver_id) and i.receiver_id.__eq__(
                        sender_id
                ):
                    return i

    def get_help_text_for_attr(self, agent_type_name: str, attr_name: str) -> str:
        """Extracts the help text for the given attribute name of the given agent type name"""
        for name, spec in self.schema.agent_type_from_name(
                agent_type_name
        ).attributes.items():
            spec: AttributeSpecs
            if name.__eq__(attr_name):
                return spec.help_text

    # self.schema.agent_types

    def generate_new_agent_id(self):
        new_id = len(self._agents) + 1
        # note: we don't control how ids have been generated for agents created from an external source
        # so we check for possible conflict and solve it
        if new_id in self._agents:
            for i in range(1, len(self._agents) + 2):
                if i not in self._agents:
                    new_id = i
                    break
        logging.debug("generated new agent id {}".format(new_id))
        return new_id

    # the given agent id can be 0 to clear the current selection
    def set_selected_agent_id(self, agent_id: int):
        assert self.is_open
        if agent_id not in self._agents:
            assert agent_id == 0 or agent_id is None
            self.selected_agent_changed.emit(None)
        else:
            self.selected_agent_changed.emit(self._agents[agent_id])

    def add_new_agent(self, agent_model: models.Agent, x: int, y: int):
        assert self.is_open
        agent_model.set_display_xy(x, y)
        self._create_agent_controller(agent_model)

        self._scenario_model.add_agent(agent_model)
        self._project_properties.set_unsaved_changes(True)
        self.revalidate_scenario()

        logging.info(
            "created new agent {} of type '{}'".format(
                agent_model.display_id, agent_model.type_name
            )
        )

    def _create_agent_controller(self, agent_model: models.Agent):
        assert self.is_open

        # accept to add the agent even if invalid
        agent_ctrl = AgentController(agent_model)
        self._agents[agent_ctrl.id] = agent_ctrl
        agent_ctrl.model_was_modified.connect(
            self._project_properties.set_unsaved_changes
        )

        logging.info("new agent {} added".format(agent_ctrl.display_id))
        self.agent_added.emit(agent_ctrl)

    def add_new_contract(self, contract_model: models.Contract):
        self._scenario_model.add_contract(contract_model)
        self._create_contract_model(contract_model)
        self._project_properties.set_unsaved_changes(True)
        self.revalidate_scenario()
        logging.info(
            "created new contract '{}' between {} and {}".format(
                contract_model.product_name,
                contract_model.display_sender_id,
                contract_model.display_receiver_id,
            )
        )

    def set_unsaved_changes(self, unsaved: bool):
        """set the unsaved changes flag for the current scenario"""
        self._project_properties.set_unsaved_changes(unsaved)

    def _create_contract_model(self, contract: models.Contract):
        assert self.is_open

        # validate sender / receiver are known
        if contract.sender_id not in self._agents:
            raise ValueError(
                "can't add contract '{}' because sender agent id '{}' is unknown".format(
                    contract.product_name, contract.sender_id
                )
            )

        if contract.receiver_id not in self._agents:
            raise ValueError(
                "can't add contract '{}' because receiver agent id '{}' is unknown".format(
                    contract.product_name, contract.receiver_id
                )
            )

        sender_ctrl = self._agents[contract.sender_id]
        receiver_ctrl = self._agents[contract.receiver_id]

        # connect agents
        sender_ctrl.model.add_output(contract.receiver_id)
        receiver_ctrl.model.add_input(contract.sender_id)

        self.contract_added.emit(sender_ctrl, receiver_ctrl, contract)

    def rearrange_layout(self):
        """rearrange agents in the graph view into the orbital layout"""

        self.auto_scale_scenario_graph(self.agent_list, True)

    def revalidate_scenario(self):
        assert self._scenario_model is not None

        try:
            fameio.SchemaValidator.ensure_is_valid_scenario(self._scenario_model)
            self._project_properties.clear_validation_errors()
        except fameio.ValidationException as e:
            err_msg = str(e)
            logging.warning("failed to validate the scenario: {}".format(err_msg))
            self._project_properties.set_validation_error(err_msg)

    def _init_scenario_model_with_non_auto_arrange(self):
        """initialize the scenario model from the current state of the scenario coords"""
        for a in self._scenario_model.agents:
            self._create_agent_controller(a)
        for c in self._scenario_model.contracts:
            self._create_contract_model(c)

        self.revalidate_scenario()
        return

    def _adjust_agent_postions(
            self,
            agent_ctrl_list: typing.List[AgentController],
            new_agent_x: int,
            new_agent_y: int,
            agent,
    ):
        """adjust the position of the agent in the scene"""

        for agent_ctrl in agent_ctrl_list:
            if agent.id.__eq__(agent_ctrl.id):
                agent_ctrl.scene_item.setPos(new_agent_x, new_agent_y)
                agent_ctrl.model_was_modified.emit()
                agent_ctrl.position_changed()
                break

    def init_scenario_model(self, scenario: models.Scenario, file_path: str):
        """init the scenario model and create the corresponding controllers.
        Build the graph orbital model and validate the scenario.
        """

        logging.debug("opening new scenario")
        rearrange_mode = False

        if self.is_open:
            rearrange_mode = True

        self.reset()

        try:
            self._scenario_model = scenario
            self._project_properties.reset(file_path)
            self._project_properties.set_unsaved_changes(True)
            if not rearrange_mode:
                self._init_scenario_model_with_non_auto_arrange()
                return

            try:
                last_list = []
                agent_type_bucket_list = self._prep_buckets_for_rearrange()

                default_radius = 100.0
                radius = 50
                margin = 20
                last_x = 0.0
                last_y = 0.0

                min_distance = (float(radius) * 2) + float(margin)

                for item in agent_type_bucket_list:
                    new_radius = default_radius * 1.1

                    if new_radius - default_radius < min_distance:
                        new_radius = new_radius + radius * 2 + margin
                    default_radius = new_radius

                    new_radius = default_radius * 1.1
                    if new_radius - default_radius < min_distance:
                        new_radius = new_radius + radius * 2 + margin
                    default_radius = new_radius

                    last_x, last_y, default_radius, new_last_list = self._adjust_agent_position(
                        item, default_radius, radius, margin, last_x, last_y
                    )
                    last_list.extend(new_last_list)

                if not rearrange_mode:
                    for a in last_list:
                        self._create_agent_controller(a)
                    for c in self._scenario_model.contracts:
                        self._create_contract_model(c)

            except Exception as e:
                logging.error("failed to init the given scenario: {}".format(e))
                self.reset()
                raise Exception(e)

            # refresh the UI
            self._project_properties.changed.emit()

            self.revalidate_scenario()
        except Exception as e:
            logging.error("failed to init the given scenario: {}".format(e))
            self.reset()
            raise

        # refresh the UI

        self._project_properties.changed.emit()

        self.revalidate_scenario()

    def save_to_file(self, file_path):
        assert self.is_open
        models.ScenarioLoader.save_to_yaml_file(self._scenario_model, file_path)
        # update status
        self._project_properties.set_unsaved_changes(False)
        self._project_properties.set_file_path(file_path)
        self.revalidate_scenario()
