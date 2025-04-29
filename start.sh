#!/bin/bash

# Espera possíveis migrações ou configurações futuras
echo "Iniciando bot com Uvicorn..."

exec uvicorn app.main:app --host=0.0.0.0 --port=${PORT:-8000}