import spacy
from spacy.language import Language
from spacy.tokens import Doc, Span


@Language.factory("denomme")
def person_name_component(nlp: Language, name: str)->Doc:
    """denomme component which imports the name-detection
    module and also combines the compund name

    Args:
        nlp (Language): spaCy Language Module
        name (str): name of the component

    Returns:
        Doc : spacy doc
    """
    return DenommeComponent(nlp)


class DenommeComponent:
    def __init__(self, nlp: Language):
        """Name detection component which extends the 
        name-ner-detection and combines compound names
        into one name that can be found under the extension
        person_name

        eg.

        doc._.person_name will return Span for the detected 
        person names in the doc

        Args:
            nlp (Language): spaCy Language Module
        """
        self.name_ner = spacy.load("xx_denomme")
        if not Doc.has_extension("person_name"):
            Doc.set_extension("person_name", default=[])

    def __call__(self, doc: Doc) -> Doc:
        name_doc = self.name_ner(doc.text)
        names = []
        for ent in name_doc.ents:
            end_search = False
            count = 1
            if ent.label_ == "S-PER":
                name = Span(doc, ent.start, ent.end, label="PERSON")
                names.append(name)
            if ent.label_ == "B-PER":
                try:
                    if doc[ent.start + 1].ent_type_ == "B-PER":
                        end_search = True
                except:
                    end_search = True

                start = ent.start
                end = ent.end
                prev_token = doc[ent.start - 1]
                if prev_token.text.title() in ("Dr", "Dr.", "Mr", "Mr.", "Ms", "Ms.", "Mrs", "Mrs."):
                    start = start - 1
                while not (end_search):
                    try:
                        next_token = doc[ent.start + count]
                        count += 1
                    except:
                        end_search = True
                    if count == 3 or next_token.ent_type_ == "E-PER":
                        end_search = True
                    end = ent.start + count
                name = Span(doc, start, end, label="PERSON")
                names.append(name)
        doc._.person_name = names
        return doc
