#!/bin/bash
# Prueba de conexión a PostgreSQL en Clever Cloud
PGPASSWORD='FNx3hlQYpt6yOuY6oXROrULrJ8jw9I' psql -h b54iyt2qxcbwagrdlwqx-postgresql.services.clever-cloud.com -p 50013 -U u1f5ksljznuhzpuyjes3 -d b54iyt2qxcbwagrdlwqx -c '\l'
