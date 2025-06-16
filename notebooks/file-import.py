from azure.storage.blob import BlobClient

# Convert DataFrame to CSV in memory
output_stream = io.StringIO()
merged_df.to_csv(output_stream, index=False)
output_stream.seek(0)

# Define target blob name
target_blob_name = "merged_output.csv"

# Upload to blob
blob_client = container_client.get_blob_client(target_blob_name)
blob_client.upload_blob(output_stream.getvalue(), overwrite=True)

print(f"✅ File uploaded successfully to 'https://{account_name}.blob.core.windows.net/{container_name}/{target_blob_name}'")
