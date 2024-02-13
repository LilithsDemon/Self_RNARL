# This allows to run design rna to be able to get data : In learnamaster/src/learna
python3 design_rna.py   --mutation_threshold 5   --batch_size 126   --conv_sizes 17 5   --conv_channels 7 18   --embedding_size 3   --entropy_regularization 6.762991409135427e-05   --fc_units 57   --learning_rate 0.0005991629320464973   --lstm_units 28   --num_fc_layers 1   --num_lstm_layers 1   --reward_exponent 9.33503385734547   --state_radius 32   --target_structure_path /external/'Small Drive'/UNI/'Year 2'/RNARL2/learnamaster/data/eterna/100.rna   --restart_timeout 1800

# This allows to run design rna to be able to get data for 10 mins : In learnamaster/src/learna
python3 design_rna.py \
  --batch_size 32 \
  --conv_channels 8 1 \
  --embedding_size 0 \
  --entropy_regularization 0.00044440579487984737 \
  --fc_units 52 \
  --learning_rate 0.000548959271057026 \
  --lstm_units 4 \
  --num_fc_layers 1 \
  --num_lstm_layers 2 \
  --optimization_steps 10 \
  --reward_exponent 5.724874982958563 \
  --mutation_threshold 5 \
  --conv_sizes 5 3 \
  --state_radius 16 \
  --likelihood_ratio_clipping 0.3 \
  --include_mutation \
  --fc_activation relu \
  --target_structure_path /external/'Small Drive'/UNI/'Year 2'/RNARL2/learnamaster/data/eterna/100.rna \
  --restart_timeout 600


- David Silver - First few

- Keep reproductions

- Re-read - Get new paper annotate