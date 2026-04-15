import uuid

from sqlalchemy import (
    ForeignKeyConstraint,
    PrimaryKeyConstraint,
    String,
    Text,
    UniqueConstraint,
    Uuid,
    text,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = "users"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="users_pkey"),
        UniqueConstraint("name", name="users_name_key"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid, primary_key=True, server_default=text("gen_random_uuid()")
    )
    name: Mapped[str] = mapped_column(Text, nullable=False)

    houses: Mapped[list["Houses"]] = relationship("Houses", back_populates="user")


class Houses(Base):
    __tablename__ = "houses"
    __table_args__ = (
        ForeignKeyConstraint(
            ["user_id"], ["users.id"], ondelete="CASCADE", name="houses_user_id_fkey"
        ),
        PrimaryKeyConstraint("id", name="houses_pkey"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid, primary_key=True, server_default=text("gen_random_uuid()")
    )
    user_id: Mapped[uuid.UUID] = mapped_column(Uuid, nullable=False)
    color: Mapped[str] = mapped_column(String(50), nullable=False)

    user: Mapped["Users"] = relationship("Users", back_populates="houses")
