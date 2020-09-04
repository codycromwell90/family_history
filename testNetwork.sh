#!/bin/bash

  host="www.google.com"
  dtm=`date` 

  ping -c1 "$host" &> /dev/null

  if [ $? -eq 0 ]; then
    echo "connection is UP - $dtm"  
  else
    echo "  connection is DOWN - $dtm"
  fi
