# Comercial ITI · Dashboard Web (versión inicial)
Ruta: `comercial/index.html`

## Abrir
Abre `comercial/index.html` en Chrome/Edge (requiere acceso a CDN para cargar SheetJS y Chart.js) y selecciona el Excel comercial local desde el selector. La lectura y los cálculos ocurren en el navegador, en memoria. **No hay datos de ITI guardados aquí.**

## Alcance
- ACTUAL MONTH, ACUMULATED BOX y SERVICIOS.
- Selector mensual, escenario REAL26 / PPTO26 / FCST 2 26, línea y servicio.
- BOX, recaladas, gráficos de estado, embarque/descarga, tamaño, servicios e historia mensual.
- Servicio ALPACA / LLAMA unificado para comparación; WS4 → WS3.
- Para una línea específica, las recaladas y BOX/recalada se muestran como no aplicables: el origen RECALADAS no contiene columna de línea.

## Validación pendiente
1. Contrastarlo con el PBIP original Commercial_ITI_Final para los tres escenarios y los doce meses.
2. Revisar los criterios de filtros y títulos visual por visual, así como los subtotales de líneas y servicios.
3. Alinear el diseño fino y las herramientas de navegación.
4. El Excel actual `datos comercial box 24.xlsx` tiene hojas `2023` y `RECALADAS`. No publicar nunca el Excel en este repositorio.

## Seguridad
Repositoro actualmente público; usar solo código genérico. Para un proyecto corporativo, convertir a privado y aprobar publicación y hosting con ITI. Las bibliotecas del CDN son de terceros; para un entorno productivo deben alojarse localmente e implantarse controles de seguridad.

El PBIP original se conserva separado. Esta versión web no sustituye al reporte oficial hasta validarse.
