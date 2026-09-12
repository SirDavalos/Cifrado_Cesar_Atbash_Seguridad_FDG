import streamlit as st
import Cifradores

st.set_page_config(page_title="Criptografo Dinamico de Cesar y Atbash", page_icon="🔐", layout="wide")

st.title(
    "Cifrado y Descifrado Dinámico de César Y Atbash",
    text_alignment = "center",
)
# --- PUNTO 5% : ALFABETO / SÍMBOLOS PERSONALIZADOS ---

st.space(size = "small")

st.header(
    "Alfabeto de Cifrado",
    text_alignment="center",
)
st.text("Aqui debe poner el codigo que se usara para cifrar")
alfabeto_input = st.text_area(
    "Puede incluir: Cualquier alfabeto (Romano, Griego, Japones), Simbolos UNICODE, O incluso Emojis!",
    placeholder="Ej: ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$",
    help="Por default, se usa el alfabeto estandar multilingüe. Siempre se usara este alfabeto a menos que se Ingrese otro alfabeto"
)


if alfabeto_input.strip():
    alfabeto = alfabeto_input.strip()
    longitud_alfabeto = len(alfabeto)
    st.success(f"Alfabeto Personalizado Detectado\n- Tamaño del Alfabeto: **{longitud_alfabeto}**")
else:
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$"
    st.info("Alfabeto Multilingüe Estándar Activo")

st.space(size = "medium")

# --- PESTAÑAS PRINCIPALES ---
tab_cifrado, tab_descifrado = st.tabs([" Cifrado de Texto ", " Descifrado Automático"])

with tab_cifrado:
    st.header(
        "Cifrado de Mensajes",
        text_alignment = "center"
    )
    col1, col2 = st.columns(2)

    with col1:
        tipo_cifrado = st.selectbox("Selecciona el algoritmo de Cifrado:", ["César", "Atbash"])

        max_key = len(alfabeto) - 1

        key = 0
        if tipo_cifrado == "César":
            desplazamiento = st.number_input(
                f"Selecciona el desplazamiento (0 a {max_key}):",
                min_value=0,
                max_value=max_key,
                value=3
            )

    with col2:
        input_text = st.text_area("Mensaje a cifrar:", "Hola Mundo! Este es un mensaje")

    if st.button("Cifrar", type="primary"):
        if tipo_cifrado == "César":
            res = Cifradores.cifrar_cesar(input_text, alfabeto, desplazamiento)
        else:
            res = Cifradores.cifrar_atbash(input_text, alfabeto)

        st.subheader("Texto Cifrado:")
        st.code(res, language=None)

with tab_descifrado:
    st.header(
        "Descifrado Automático",
        text_alignment="center"
    )
    texto_cif = st.text_area("Mensaje cifrado a decriptar:", "")

    if st.button("Analizar y Descifrar", type="primary"):
        if texto_cif.strip():
            mejor_decifrado = Cifradores.conseguir_descifrado(texto_cif, alfabeto)
            mensaje_descifrado = ""
            if Cifradores.probar_atbash(texto_cif, alfabeto, mejor_decifrado):
                tipo_cifrado = "Atbash"
                mejor_decifrado = Cifradores.cifrar_atbash(texto_cif, alfabeto)
                mensaje_descifrado = mejor_decifrado
            else:
                tipo_cifrado = "Cesar"
                mensaje_descifrado = mejor_decifrado['texto']

            st.success("Mensaje Decriptado")
            res_col1, res_col2 = st.columns(2)

            with res_col1:
                st.markdown("###  Método y Módulo Detectados")
                st.write(f"*Metodo de Cifrado Detectados: * {tipo_cifrado}")
                if tipo_cifrado == 'César':
                    st.write(f"Desplazamiento:* {mejor_decifrado['desplazamiento']}")

            with res_col2:
                st.markdown("###  Texto Descifrado")
                st.code(mensaje_descifrado)
        else:
            st.warning("Por favor ingresa un texto cifrado.")