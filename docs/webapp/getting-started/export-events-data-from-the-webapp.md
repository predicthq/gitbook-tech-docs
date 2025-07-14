# Export Events Data from the WebApp

The exporter feature allows you to export our events data in CSV or JSONL format directly from the WebApp - Events Search, enabling you to use this data locally on your computer, or for other use cases. It’s easy to get started.

### **What’s Supported?** <a href="#object-object" id="object-object"></a>

PredictHQ currently supports the export of real-world events and Live TV events.

You can export large volumes of data using the exporter. It runs in the background and you can continue using the WebApp while it runs.

### **How Can I Export Data?** <a href="#object-object-1" id="object-object-1"></a>

1. Visit the [Events Search](https://control.predicthq.com/search/events) within the WebApp
2. Search for events with the filters and ranges you want to be applied
3.  Press the “Export” button above the search results

    <figure><img src="https://images.ctfassets.net/ihlmn42cjuv0/3caKGQhtkJYZIyijaGm7xk/749d021d5181b66e04f0218bf620cbda/Screenshot_2024-06-07_100127.png" alt="Export option in CC"><figcaption></figcaption></figure>
4. A dialog will appear, select the format you would like to export the file in - CSV or JSONL
5. The data exporter will begin processing your export. If it’s small, the export will be available soon on the pop-up (click refresh in the dialog to see the latest status). For larger exports of tens of thousands of records or more they may take some time. You can continue using the WebApp while the export runs. There is no need to keep the dialog open to wait for it to complete.
6. You will receive an email when the export is ready for download. Click on the button in the file to download your exported file. The file will be a ZIP file containing the formatted data of your choice.

<figure><img src="https://images.ctfassets.net/ihlmn42cjuv0/76a1U3Zi3DfSl8SRRl0nRk/d1c866be54e1994b68e54bd6d660a037/exp1.PNG" alt="export email" height="720" width="726"><figcaption><p>Example of the email you'll receive once your exported file is ready to download</p></figcaption></figure>

### Viewing Export Status and Previous Exports <a href="#viewing-export-status-and-previous-exports" id="viewing-export-status-and-previous-exports"></a>

To view previously exported files or check the progress of a current export choose "Previous Exports" from the export menu. This will open a dialog showing a list of previously exported files. It will also show any exports that are in progress and being processed. In progress exports will showing as "processing". Completed exports will have a green tick and indicate the file size.

From this screen you can download exports or delete exports.

<figure><img src="https://images.ctfassets.net/ihlmn42cjuv0/3a8jDk85d5n0YpqDsfklPd/4fd92518953b41a43cb035eb2d69d7d2/Screenshot_2024-06-07_100436.png" alt="Exported Files Dialog"><figcaption></figcaption></figure>

### Export File Format <a href="#export-file-format" id="export-file-format"></a>

See the [Events API Response Fields documentation](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/events/search-events) or the [OpenAPI Spec](https://api.predicthq.com/docs/?urls.primaryName=Events+API) for information on the fields included in the export.

JSONL format exports are very similar to the Events API response.

CSV exports have some fields split into "normalized" fields.

### **When are exports deleted?** <a href="#object-object-2" id="object-object-2"></a>

We encourage you to download your export as soon as it’s ready. At the moment we store exports for 30 days.
