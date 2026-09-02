cd "D:\Danilo\Trading\Cursor Trading"
# Regenerar los 3 live + probabilidad ML
python analyze_btc_m5.py --mode all --no-chart --ml
# Re-entrenar (recomendado: 1× por semana, ~3 min con caché)
python train_btc_signals.py