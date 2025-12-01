#!/bin/bash

pg_dump -d fwm -h localhost -p 5433 -U  fwm -c -f fwm_dump.sql
psql -U postgres -d fwm < fwm_dump.sql

# Reset all sequences to prevent primary key conflicts
psql -U postgres -d fwm -c "SELECT setval(pg_get_serial_sequence('archiv_geography', 'id'), COALESCE((SELECT MAX(id) FROM archiv_geography), 1), true);"
psql -U postgres -d fwm -c "SELECT setval(pg_get_serial_sequence('archiv_institution', 'id'), COALESCE((SELECT MAX(id) FROM archiv_institution), 1), true);"
psql -U postgres -d fwm -c "SELECT setval(pg_get_serial_sequence('archiv_quarry', 'id'), COALESCE((SELECT MAX(id) FROM archiv_quarry), 1), true);"
psql -U postgres -d fwm -c "SELECT setval(pg_get_serial_sequence('archiv_quarrygroup', 'id'), COALESCE((SELECT MAX(id) FROM archiv_quarrygroup), 1), true);"
psql -U postgres -d fwm -c "SELECT setval(pg_get_serial_sequence('archiv_sample', 'id'), COALESCE((SELECT MAX(id) FROM archiv_sample), 1), true);"
psql -U postgres -d fwm -c "SELECT setval(pg_get_serial_sequence('archiv_artifact', 'id'), COALESCE((SELECT MAX(id) FROM archiv_artifact), 1), true);"
psql -U postgres -d fwm -c "SELECT setval(pg_get_serial_sequence('archiv_analyse', 'id'), COALESCE((SELECT MAX(id) FROM archiv_analyse), 1), true);"
psql -U postgres -d fwm -c "SELECT setval(pg_get_serial_sequence('archiv_number', 'id'), COALESCE((SELECT MAX(id) FROM archiv_number), 1), true);"
psql -U postgres -d fwm -c "SELECT setval(pg_get_serial_sequence('archiv_images', 'id'), COALESCE((SELECT MAX(id) FROM archiv_images), 1), true);"
psql -U postgres -d fwm -c "SELECT setval(pg_get_serial_sequence('archiv_project', 'id'), COALESCE((SELECT MAX(id) FROM archiv_project), 1), true);"
