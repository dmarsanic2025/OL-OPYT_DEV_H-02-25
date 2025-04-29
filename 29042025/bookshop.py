import sqlalchemy as db
from sqlalchemy.orm import declarative_base, relationship, backref, sessionmaker

Base = declarative_base()

autor_izdavac = db.Table(
    "autor_izdavac",
    Base.metadata,
    db.Column("autor_id", db.Integer, db.ForeignKey("autor.id")),
    db.Column("izdavac_id", db.Integer, db.ForeignKey("izdavac.id")),
)

knjiga_izdavac = db.Table(
    "knjiga_izdavac",
    Base.metadata,
    db.Column("knjiga_id", db.Integer, db.ForeignKey("knjiga.id")),
    db.Column("izdavac_id", db.Integer, db.ForeignKey("izdavac.id")),
)


class Autor(Base):
    __tablename__ = "autor"
    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String)
    prezime = db.Column(db.String)

    knjige = relationship("Knjiga", backref=backref("autor"))
    izdavaci = relationship("Izdavac", secondary=autor_izdavac, back_populates="autori")


class Knjiga(Base):
    __tablename__ = "knjiga"
    id = db.Column(db.Integer, primary_key=True)
    autori_id = db.Column(db.Integer, db.ForeignKey("autor.id"))
    naslov = db.Column(db.String)

    izdavaci = relationship(
        "Izdavac", secondary=knjiga_izdavac, back_populates="knjige"
    )


class Izdavac(Base):
    __tablename__ = "izdavac"
    id = db.Column(db.Integer, primary_key=True)
    naziv = db.Column(db.String)

    autori = relationship("Autor", secondary=autor_izdavac, back_populates="izdavaci")
    knjige = relationship("Knjiga", secondary=knjiga_izdavac, back_populates="izdavaci")


def add_knjiga(session, ime_autora, naslov_knjige, naziv_izdavaca):
    ime, _, prezime = ime_autora.partition(" ")

    knjiga = (
        session.query(Knjiga)
        .join(Autor)
        .filter(Knjiga.naslov == naslov_knjige)
        .filter(db.and_(Autor.ime == ime, Autor.prezime == prezime))
        .filter(Knjiga.izdavaci.any(Izdavac.naziv == naziv_izdavaca))
        .one_or_none()
    )
    if knjiga is not None:
        return

    if knjiga is None:
        knjiga = Knjiga(naslov=naslov_knjige)

    autor = (
        session.query(Autor)
        .filter(db.and_(Autor.ime == ime, Autor.prezime == prezime))
        .one_or_none()
    )

    if autor is None:
        autor = Autor(ime=ime, prezime=prezime)
        session.add(autor)

    izdavac = (
        session.query(Izdavac).filter(Izdavac.naziv == naziv_izdavaca).one_or_none()
    )

    if izdavac is None:
        izdavac = Izdavac(naziv=naziv_izdavaca)
        session.add(izdavac)

    knjiga.autor = autor
    knjiga.izdavaci.append(izdavac)
    session.add(knjiga)

    session.commit()


def main():
    db_engine = db.create_engine("sqlite:///book_shop.db")

    Base.metadata.create_all(db_engine)

    Session = sessionmaker(bind=db_engine)
    session = Session()

    nove_knjige = [
        ["Isaac Asimov", "Foundation", "Random House"],
        ["Pearl Buck", "The Good Earth", "Random House"],
        ["Pearl Buck", "The Good Earth", "Simon & Schuster"],
        ["Tom Clancy", "The Hunt For Red October", "Berkley"],
        ["Tom Clancy", "Patriot Games", "Simon & Schuster"],
        ["Stephen King", "It", "Random House"],
        ["Stephen King", "It", "Penguin Random House"],
        ["Stephen King", "Dead Zone", "Random House"],
        ["Stephen King", "The Shining", "Penguin Random House"],
        [
            "John Le Carre",
            "Tinker, Tailor, Soldier, Spy: A George Smiley Novel",
            "Berkley",
        ],
        ["Alex Michaelides", "The Silent Patient", "Simon & Schuster"],
        ["Carol Shaben", "Into The Abyss", "Simon & Schuster"],
    ]

    for knjiga in nove_knjige:
        add_knjiga(
            session,
            ime_autora=knjiga[0],
            naslov_knjige=knjiga[1],
            naziv_izdavaca=knjiga[2],
        )

    # TODO
    # get_knjige_po_izdavacu()
    # get_autore_po_izdavacu()
    # get_autori()


if __name__ == "__main__":
    main()
