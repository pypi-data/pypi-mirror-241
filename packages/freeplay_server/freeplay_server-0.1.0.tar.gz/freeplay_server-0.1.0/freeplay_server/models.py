import uuid
from _decimal import Decimal
from datetime import datetime
from typing import Any, Optional

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, Numeric, UniqueConstraint, Table, Column, ARRAY
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship
from sqlalchemy.orm import Mapped

from freeplay_server.comparisons.comparisons import ComparisonType
from freeplay_server.extensions import sa
from freeplay_server.project_sessions.project_sessions import ProjectSessionCalculator


class Base(DeclarativeBase):
    pass


class Project(Base):
    __tablename__ = 'projects'

    id: Mapped[uuid.UUID] = mapped_column(UUID(), primary_key=True,
                                          server_default=sa.text('gen_random_uuid()'))


class PromptTemplate(Base):
    __tablename__ = 'prompt_templates'

    id: Mapped[uuid.UUID] = mapped_column(UUID(), primary_key=True,
                                          server_default=sa.text('gen_random_uuid()'))
    project_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(Project.id), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    criteria: Mapped[list["EvaluationCriteria"]] = relationship("EvaluationCriteria", lazy="selectin")


class ProjectSession(Base):
    __tablename__ = 'project_sessions'

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True,
                                          server_default=sa.text('gen_random_uuid()'))
    test_run_id: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey("test_runs.id"), nullable=True)
    project_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(Project.id, ondelete='CASCADE'), nullable=False)
    start_time: Mapped[datetime] = mapped_column(DateTime(timezone=False), nullable=False)
    entries: Mapped[list["ProjectSessionEntry"]] = relationship("ProjectSessionEntry", lazy="selectin")
    evaluation_results: Mapped[list["EvaluationResult"]] = relationship("EvaluationResult", lazy="selectin")

    def first_inputs(self) -> dict[str, str]:
        return self.entries[0].inputs_dict()

    def last_response(self) -> str:
        return self.entries[-1].response

    def cost(self) -> Decimal:
        return sum([ProjectSessionCalculator.calculate_costs(
            entry.prompt_token_cost, entry.response_token_cost
        ) or Decimal(0) for entry in self.entries], Decimal(0))

    def latency(self) -> Decimal:
        return sum([
            ProjectSessionCalculator.calculate_latency(
                entry.start_time, entry.end_time
            ) or Decimal(0) for entry in self.entries], Decimal(0))


class LLMFlavor(Base):
    __tablename__ = 'llm_flavors'

    id: Mapped[uuid.UUID] = mapped_column(UUID(), primary_key=True,
                                          server_default=sa.text('gen_random_uuid()'))
    name: Mapped[str] = mapped_column(String, nullable=False)
    provider_name: Mapped[str] = mapped_column(String, nullable=False)


class LLMModel(Base):
    __tablename__ = 'llm_models'

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True,
                                          server_default=sa.text('gen_random_uuid()'))
    name: Mapped[str] = mapped_column(String, nullable=False)
    flavor_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(LLMFlavor.id), nullable=False)
    is_visible: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    flavor: Mapped[LLMFlavor] = relationship(LLMFlavor, lazy="joined")


class Environment(Base):
    __tablename__ = 'environments'
    __table_args__ = (
        UniqueConstraint('name'),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True,
        server_default=sa.text('gen_random_uuid()')
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    created_date: Mapped[datetime] = mapped_column(DateTime(timezone=False), nullable=False)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)


class ProjectSessionEntry(Base):
    __tablename__ = 'project_session_entries'

    id: Mapped[uuid.UUID] = mapped_column(UUID(), primary_key=True,
                                          server_default=sa.text('gen_random_uuid()'))
    logged_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), nullable=False)
    project_session_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(ProjectSession.id), nullable=False)
    prompt_template_id: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey(PromptTemplate.id))
    prompt: Mapped[str] = mapped_column(String, nullable=False)
    response: Mapped[str] = mapped_column(String, nullable=False)
    format_type: Mapped[str] = mapped_column(String)
    is_complete: Mapped[bool] = mapped_column(Boolean)
    prompt_token_count: Mapped[int] = mapped_column(Integer)
    response_token_count: Mapped[int] = mapped_column(Integer)
    prompt_token_cost: Mapped[Optional[float]] = mapped_column(Numeric)
    response_token_cost: Mapped[Optional[float]] = mapped_column(Numeric)
    # TODO: We will introduce a class for PromptTemplateVersion and make this a foreign key+relationship.
    prompt_template_version_id: Mapped[Optional[uuid.UUID]] = mapped_column(UUID())
    model_id: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey(LLMModel.id))
    start_time: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=False))
    end_time: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=False))
    function_call_response: Mapped[Optional[dict[str, Any]]] = mapped_column(JSONB)
    api_key_last_four: Mapped[Optional[str]] = mapped_column(String)
    api_key_name: Mapped[Optional[str]] = mapped_column(String)
    environment_id: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey(Environment.id), nullable=True)

    model: Mapped[Optional[LLMModel]] = relationship(LLMModel, lazy="joined")
    prompt_template: Mapped[PromptTemplate] = relationship(PromptTemplate, lazy="joined")
    inputs: Mapped[list["ProjectSessionEntryInputs"]] = relationship("ProjectSessionEntryInputs", lazy="selectin")
    environment: Mapped[Optional[Environment]] = relationship(Environment, lazy="selectin")

    def inputs_dict(self) -> dict[str, str]:
        return {input.name: input.value for input in self.inputs}


class ProjectSessionEntryInputs(Base):
    __tablename__ = 'project_session_entry_inputs'

    project_session_entry_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(ProjectSessionEntry.id), nullable=False,
                                                                primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False, primary_key=True)
    value: Mapped[str] = mapped_column(String, nullable=False)


class EvaluationCriteria(Base):
    __tablename__ = 'evaluation_criterias'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True,
                                          server_default=sa.text('gen_random_uuid()'))
    name: Mapped[str] = mapped_column(String(), nullable=False)
    question: Mapped[str] = mapped_column(String(), nullable=False)

    llm_question: Mapped[str] = mapped_column(String(), nullable=True)
    llm_eval_enabled: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    # yes-no or 1-5 for now
    type: Mapped[str] = mapped_column(String(), nullable=False)

    prompt_template_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(PromptTemplate.id, ondelete='CASCADE'),
                                                          nullable=False)

    prompt_template: Mapped[PromptTemplate] = relationship(PromptTemplate, lazy='selectin', back_populates='criteria')
    rubric: Mapped[list["EvaluationRubric"]] = relationship("EvaluationRubric", lazy="selectin")


# Corresponds to one score/label of a rubric.
class EvaluationRubric(Base):
    __tablename__ = 'evaluation_rubrics'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True,
                                          server_default=sa.text('gen_random_uuid()'))
    criteria_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(EvaluationCriteria.id),
                                                   nullable=False)

    # The score/label that this rubric corresponds to, e.g. 'yes', 'no', 1, 2, 3, 4, 5.
    score: Mapped[Any] = mapped_column(JSONB, nullable=False)

    # The actual rubric instructions for a given score, "A 1 on the friendliness scale uses rude words.."
    instructions: Mapped[str] = mapped_column(String(), nullable=False)


class EvaluationResult(Base):
    __tablename__ = 'evaluation_results'
    __table_args__ = (
        UniqueConstraint('evaluation_criteria_id', 'session_id'),
    )

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True,
                                          server_default=sa.text('gen_random_uuid()'))
    evaluation_criteria_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(EvaluationCriteria.id),
                                                              nullable=False)
    session_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(ProjectSession.id), nullable=False)

    # 'yes', 'no', 1, 2, 3, 4, 5.
    manual_score: Mapped[Optional[Any]] = mapped_column(JSONB, nullable=True)
    auto_eval_score: Mapped[Optional[Any]] = mapped_column(JSONB, nullable=True)

    def score(self) -> Optional[Any]:
        if self.manual_score:
            return self.manual_score
        else:
            return self.auto_eval_score


    criterion: Mapped[EvaluationCriteria] = relationship(EvaluationCriteria)


# Mapping table for many:many test list <> test cases
test_list_test_cases = Table(
    'test_list_test_cases',
    Base.metadata,
    Column('created_at', DateTime(timezone=False), server_default=sa.text('now()')),
    Column('test_case_id', ForeignKey('test_cases.id')),
    Column('test_list_id', ForeignKey('test_lists.id'))
)


class TestList(Base):
    __tablename__ = 'test_lists'
    # Columns
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True,
                                          server_default=sa.text('gen_random_uuid()'), nullable=False)
    project_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(Project.id), nullable=False)
    name: Mapped[str] = mapped_column(String(), nullable=False)
    description: Mapped[str] = mapped_column(String(), nullable=True)
    input_keys: Mapped[Optional[list[str]]] = mapped_column(ARRAY(String()), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), server_default=sa.text('now()'),
                                                 nullable=False)
    deleted_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=False), nullable=True)

    # Relationships
    test_cases: Mapped[list["TestCase"]] = relationship(
        "TestCase", secondary=test_list_test_cases)

    def num_test_cases(self) -> int:
        return len(self.test_cases)


test_run_comparison = Table(
    'comparison_test_runs',
    Base.metadata,
    Column('test_run_id', ForeignKey('test_runs.id')),
    Column('comparison_id', ForeignKey('comparisons.id'))
)


class TestRun(Base):
    __tablename__ = 'test_runs'
    # Columns
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=sa.text('gen_random_uuid()'),
        nullable=False)
    test_list_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey(TestList.id, ondelete="CASCADE"),
                                                    nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), server_default=sa.text('now()'),
                                                 nullable=False)

    # Relationships
    test_list: Mapped[TestList] = relationship(TestList)
    comparisons = relationship("Comparison", secondary=test_run_comparison, viewonly=True)
    project_sessions: Mapped[list[ProjectSession]] = relationship(ProjectSession, lazy="selectin")


class TestCase(Base):
    __tablename__ = 'test_cases'
    # Columns
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=sa.text('gen_random_uuid()'),
        nullable=False
    )
    inputs: Mapped[dict[str, str]] = mapped_column(JSONB, nullable=False)
    created_from_session_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey(ProjectSession.id),
        UniqueConstraint(ProjectSession.id), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=False),
        server_default=sa.text('now()'),
        nullable=False)
    uploaded_output: Mapped[Optional[str]] = mapped_column(String(), nullable=True)

    # Relationships
    test_lists: Mapped[list[TestList]] = relationship(TestList, secondary=test_list_test_cases, viewonly=True)
    created_from_session = relationship(ProjectSession, lazy="selectin")


class TestCaseComparison(Base):
    __tablename__ = 'test_case_comparisons'
    # Columns
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        server_default=sa.text('gen_random_uuid()'))
    comparison_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('comparisons.id'), nullable=False)
    test_case_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey(TestCase.id), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=False),
        server_default=sa.text('now()'),
        nullable=False)

    sort_order: Mapped[Optional[int]] = mapped_column(Integer(), nullable=True)
    preferred_test_run_id: Mapped[Optional[uuid.UUID]] = mapped_column(UUID(as_uuid=True), ForeignKey(TestRun.id))
    preferred_original: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)
    is_scored: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    # Relationships
    test_case: Mapped[TestCase] = relationship(TestCase, backref="test_case_comparisons")


class Comparison(Base):
    __tablename__ = 'comparisons'
    # Columns
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True,
                                          server_default=sa.text('gen_random_uuid()'))
    # "Needs Review", "Ended", or "Deployed".
    status: Mapped[str] = mapped_column(String(), nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), server_default=sa.text('now()'))
    comparison_type: Mapped[ComparisonType] = mapped_column(String(), nullable=False, default='vs_original')

    # Relationships
    test_case_comparisons: Mapped[list[TestCaseComparison]] = relationship(
        TestCaseComparison,
        backref="comparison",
        order_by=TestCaseComparison.sort_order.desc())
    test_runs: Mapped[list[TestRun]] = relationship(TestRun, secondary=test_run_comparison)

    def first_test_run(self) -> TestRun:
        if len(self.test_runs) > 0:
            return self.test_runs[0]
        else:
            raise RuntimeError(f"Comparison id: {self.id} did not contain test_run_id.")


class User(Base):
    __tablename__ = 'users'

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=sa.text('gen_random_uuid()')
    )
    first_name: Mapped[str] = mapped_column(String(), nullable=False, default='')
    last_name: Mapped[str] = mapped_column(String(), nullable=False, default='')
    email_address: Mapped[str] = mapped_column(String(), nullable=False)
    stytch_user_id: Mapped[str] = mapped_column(String(), nullable=False)
    is_internal: Mapped[Optional[bool]] = mapped_column(Boolean)

    account_user: Mapped["AccountUser"] = relationship("AccountUser", lazy='joined', back_populates='user')


class Role(Base):
    __tablename__ = 'roles'

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=sa.text('gen_random_uuid()')
    )
    name: Mapped[str]


# Mapping table for user -> roles
user_account_roles = Table(
    'user_account_roles',
    Base.metadata,
    Column('user_account_id', ForeignKey("users_accounts.id")),
    Column('role_id', ForeignKey(Role.id))
)


class AccountUser(Base):
    __tablename__ = 'users_accounts'

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=sa.text('gen_random_uuid()')
    )
    account_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('accounts.id'))
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey(User.id))

    user: Mapped[User] = relationship(User, lazy='joined', back_populates='account_user')
    roles: Mapped[list[Role]] = relationship("Role", lazy='selectin', secondary=user_account_roles)


# An account is a group of users, like an organization or workspace in Slack.
# Some users might be in multiple 'accounts'.
class Account(Base):
    __tablename__ = 'accounts'
    __table_args__ = (
        UniqueConstraint('name'),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=sa.text('gen_random_uuid()')
    )
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    tos_accepted_date: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=False), nullable=True)
    tos_accepted_user_email: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
