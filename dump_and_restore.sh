#!/bin/bash

pg_dump -d fwm -h localhost -p 5433 -U  fwm -c -f fwm_dump.sql
psql -U postgres -d fwm < fwm_dump.sql
