#!/bin/bash
CUR_DIR=$(cd .. && pwd)
for d in $CUR_DIR/datasets/*; do
  if [ -d $d ]; then
    dataset=$(basename $d)
    dataset="SonyAIBORobotSurface"
    DATASET_DIR=$CUR_DIR/datasets/$dataset
    echo ""
    echo "Executing dataset [ $dataset ]  ..."
    python3 ../crossvalidation.py $CUR_DIR $dataset $DATASET_DIR/"$dataset"_TRAIN.arff 1 20 1
    echo "Classification process [ $dataset ] finished"
    exit 0
  fi
done
