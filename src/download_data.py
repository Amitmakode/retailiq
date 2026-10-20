import kagglehub

# Download the Olist Brazilian e-commerce dataset from Kaggle
path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")
print("Dataset downloaded to:", path)