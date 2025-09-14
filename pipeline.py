# pipeline.py
import logging
from datetime import datetime
from config.config import PROCESSED_PATH
from etl.extract import extract
from etl.transform import transform
from etl.load import load
from etl.summary import export_summary
from etl.visualize import plot_top_locations
from etl.archive import archive_file
from etl.notify import send_email
from etl.upload import get_drive, upload_to_drive

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

if __name__ == "__main__":
    try:
        run_ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        date_folder = datetime.now().strftime("%Y-%m-%d")

        # ETL
        df = extract()
        df, summary = transform(df)
        load(df)

        # Console summary
        print("\n📊 Summary Report")
        print(f"Total incidents processed: {summary['total_rows']}")
        print(f"Time range: {summary['start_time']} to {summary['end_time']}")
        print(f"Most common location: {summary['most_common_location']}")
        print("\nTop 5 Locations:")
        for location, count in summary["top_5_locations"].items():
            print(f"- {location}: {count} incidents")

        # Artifacts
        summary_csv_path = export_summary(summary)
        chart_path = plot_top_locations(summary)
        zip_path = archive_file(PROCESSED_PATH)

        # Authenticate ONCE for Google Drive
        drive = get_drive()

        # Uploads using the same drive session
        upload_to_drive(
            PROCESSED_PATH, drive,
            root_folder="SmartTrafficPipeline",
            subfolder=date_folder,
            upload_name=f"traffic_clean_{run_ts}.csv"
        )
        upload_to_drive(
            summary_csv_path, drive,
            root_folder="SmartTrafficPipeline",
            subfolder=date_folder,
            upload_name=f"summary_{run_ts}.csv"
        )
        upload_to_drive(
            chart_path, drive,
            root_folder="SmartTrafficPipeline",
            subfolder=date_folder,
            upload_name=f"top_locations_{run_ts}.png"
        )
        upload_to_drive(
            zip_path, drive,
            root_folder="SmartTrafficPipeline",
            subfolder=date_folder,
            upload_name=f"traffic_clean_{run_ts}.zip"
        )

        # Email alert
        email_body = (
            f"SmartTrafficPipeline completed successfully ✅\n\n"
            f"Total incidents: {summary['total_rows']}\n"
            f"Most common location: {summary['most_common_location']}\n"
            f"Files uploaded to Drive folder: SmartTrafficPipeline/{date_folder}\n"
        )
        send_email("✅ Pipeline Completed", email_body)

        logging.info("Pipeline completed")
        print("✅ Pipeline completed successfully")

    except Exception as e:
        logging.error(str(e))
        print("❌ Pipeline failed:", str(e))
