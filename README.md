# Kindle Offline Kit

Configurá tu Kindle con ayuda de **Claude Code o Codex** para leer EPUB y consultar diccionarios sin Wi-Fi, conservando el lector Amazon.

**La IA te ayuda en la PC; no se instala IA en el Kindle.** Pensado para el tren: libros locales y pocos cambios.

Caso documentado: **Paperwhite12.ª generación,7 pulgadas/PW6, firmware5.20.1**, KOReader v2026.07.1. Una experiencia individual, no compatibilidad universal. No hay jailbreak automático ni binarios en este repositorio.

## Empezar: pegá esto en tu agente

~~~text
Leé README.md, AGENTS.md y docs/RUNBOOK.md de este repositorio.
Quiero leer sin Wi-Fi: conservar Amazon y mis datos, añadir KOReader
y diccionarios offline sólo si mi modelo/firmware son compatibles.
Empezá con inspección de lectura y respaldo FUERA del repositorio.
Verificá fuentes oficiales actuales; no extrapoles el caso PW6.
Presentá modelo, firmware, respaldo, método, riesgos y reversión.
Esperá mi aprobación explícita antes de modificar el Kindle.
No agregues IA, servidores, Tailscale ni debloat masivo.
Si ya está configurado, auditá sin reinstalar ni repetir parches.
Si falta un toque físico, explicá uno concreto y por qué.
~~~

Abrí esta carpeta con Codex o Claude Code y pegá el texto. Necesitás un agente con acceso local a archivos/terminal y navegación, revisando sus permisos. CLAUDE.md remite a las mismas reglas de AGENTS.md. Una sesión de chat sin acceso a tu PC puede orientar, pero no controla el USB ni la pantalla. [Prompt completo](prompts/START_HERE.md).

## Paso a paso

1. **Identificá el equipo:** modelo exacto y firmware desde Información del dispositivo, batería cargada y cable de datos. No publiques serial/cuenta.
2. **Si ya hay KOReader, salí normalmente** a Biblioteca Amazon antes del USB cuando sea necesario. PW6 usa MTP en Windows; no inventar una letra de unidad.
3. **Respaldá primero:** dos adquisiciones privadas del almacenamiento visible, documentos/sidecars y árbol KOReader si existe. Verificá rutas/hashes y límites. [Respaldo](docs/BACKUP.md).
4. **Comprobá compatibilidad en vivo:** leé [introducción](https://kindlemodding.org/jailbreaking/), [FAQ](https://kindlemodding.org/jailbreaking/jailbreak-faq.html) y [selector](https://kindlemodding.org/jailbreaking/wizard/). Si no acepta tu combinación exacta, detenerse. Hay una discrepancia documental registrada en [compatibilidad](docs/COMPATIBILITY.md).
5. **Aprobá el plan concreto:** archivos/procedencia, método, respaldo, riesgos y recuperación real. Conectar USB no autoriza todo. Algunas acciones requieren toques físicos.
6. **Seguí el método oficial elegido**, sin mezclar exploits o generaciones. La [guía KOReader](https://github.com/koreader/koreader/wiki/Installation-on-Kindle-devices) documenta KPM con Véra; revisar el paquete vigente. No reinstalar un dispositivo que ya funciona.
7. **Configurá lectura offline:** EPUB autorizados, diccionarios licenciados, vocabulario y disposición cómoda. [Lectura y diccionarios](docs/OFFLINE_READING.md).
8. **Probá un libro y una palabra reales**, suspensión/despertar, página/notas y modo avión. Portadas Amazon y KOReader son pruebas distintas. [Runbook](docs/RUNBOOK.md).
9. **Usalo antes de sumar más:** no hacen falta IA, servidores, VPN o daemons para leer archivos locales.

## Qué ofrece y qué no

KOReader permite EPUB, ajustes de lectura, diccionarios offline y vocabulario. Conservá Amazon para sus libros y progreso. Diccionarios, notas y posiciones de ambos lectores son independientes. No se incluye retirada de DRM ni migración automática de progreso.

La portada nativa depende de ajustes, anuncios y firmware: [caso y controles](docs/COVERS.md). Una portada no prueba que desaparecieron anuncios de Inicio/tienda ni que el equipo sea más rápido. No hay benchmark de autonomía o rendimiento.

## Verificar dos copias locales

Python3.10+, biblioteca estándar, sin paquetes de terceros. La herramienta **no copia archivos ni lee MTP**: compara dos carpetas ya adquiridas. Nunca escribe en las entradas. El reporte incluye nombres de archivos y debe quedar privado, fuera del repo.

~~~powershell
python tools/verify_backup.py --source "D:\KindlePrivate\acquisition-a" --backup "D:\KindlePrivate\acquisition-b" --report "D:\KindlePrivate\verification.private.json"
~~~

Reemplazá las rutas por carpetas reales existentes fuera del repositorio. Código0: iguales;1: diferencias;2: error/precondición insegura. Igualdad de hashes no demuestra cobertura completa ni recuperación de rootfs. Si no tenés Python, podés seguir la guía y usar un verificador existente; nada se instala automáticamente.

## Evidencia y límites

- [Caso documentado](docs/TESTED_CASE.md): un PW6 y pruebas concretas.
- [Fuentes/repositorios/redes](docs/SOURCES.md): enlaces, fecha, clasificación y acceso.
- [Problemas frecuentes](docs/TROUBLESHOOTING.md), [seguridad](SECURITY.md), [contribuir](CONTRIBUTING.md).

Sin afiliación con Amazon, KindleModding, KOReader, Anthropic u OpenAI. No se publican libros, diccionarios, firmware, exploits, respaldos, fotos, credenciales o scripts generados para un dispositivo privado. MIT para nuestro material original; lo enlazado conserva sus licencias.

**English:** An agent-assisted, offline-first Kindle guide. Use the starter prompt and ask the agent to answer in your language. Verify exact model/firmware, preserve private data outside Git, approve device writes after a concrete plan, and test actual offline reading. This is not a universal one-click jailbreak.
