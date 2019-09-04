import pipelines

item = {
    'name': "a",
    'address': "adada"
}

csv = pipelines.CsvWriterPipeline()
csv.open_spider(None)
csv.process_item(item, None)
csv.process_item(item, None)
