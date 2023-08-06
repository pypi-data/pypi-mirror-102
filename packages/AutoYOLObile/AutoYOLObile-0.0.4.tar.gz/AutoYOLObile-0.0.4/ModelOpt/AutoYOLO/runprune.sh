python train.py --device 0,1,2,3 --admm --epoch 25 --sparsity-type block-punched --config-file config_csdarknet53pan_v14
echo finish admm process
python train.py --device 0,1,2,3 --masked-retrain --epoch 280  --sparsity-type block-punched --config-file config_csdarknet53pan_v14 --multi-scale
echo finish retrain
python test.py --device 0 --weights weights/best8x-514.pt
