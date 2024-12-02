from io import BytesIO

import face_recognition

def get_encodings_from_uploaded_file(uploaded_file):
    """
    Cette fonction reçoit un fichier téléchargé (type InMemoryUploadedFile ou TemporaryUploadedFile)
    et retourne les encodages des visages détectés dans ce fichier.
    """
    try:
        # Lire l'image depuis le fichier téléchargé en mémoire
        face_image = face_recognition.load_image_file(BytesIO(uploaded_file.read()))

        # Détecter les positions des visages dans l'image
        face_locations = face_recognition.face_locations(face_image)

        if not face_locations:
            return None  # Retourner None si aucune face n'est trouvée

        # Obtenir les encodages des visages
        face_encodings = face_recognition.face_encodings(face_image, face_locations)

        if face_encodings:
            return face_encodings[0]  # Retourner le premier encodage (si plusieurs visages, ajustez selon besoin)
        return None  # Retourner None si aucun encodage n'a été généré

    except Exception as e:
        # Gestion des erreurs si l'image n'est pas valide ou une autre erreur se produit
        print(f"Erreur lors de la génération de l'encodage: {e}")
        return None

def get_encodings(image_location: str):

    face_image = face_recognition.load_image_file(image_location)
    face_locations = face_recognition.face_locations(face_image)
    face_encodings = face_recognition.face_encodings(face_image, face_locations)

    return face_encodings


def get_face_matches(first_image_location: str, second_image_location: str):

    first_face_encodings = get_encodings(first_image_location)
    second_face_encodings = get_encodings(second_image_location)

    result = face_recognition.compare_faces(first_face_encodings, second_face_encodings)

    return result