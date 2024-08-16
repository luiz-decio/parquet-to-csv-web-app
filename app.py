import io
import pandas as pd
import streamlit as st

def main():
    st.title("File Converter")

    # Selection of conversion type
    option = st.selectbox("Choose conversion", ["Parquet to CSV", "CSV to Parquet"])
    
    loaded_file = st.file_uploader(f"Load your {option.split()[0]} file", type=[option.split()[0].lower()])

    if option == "CSV to Parquet":
        option_2 = st.selectbox("Choose delimiter", [";", ","])

    if loaded_file is not None:
        try:
            if option == "Parquet to CSV":
                # Read the parquet file into a pandas Dataframe
                df = pd.read_parquet(io.BytesIO(loaded_file.getvalue()))

                # Show a basic preview of the file
                st.write("Preview")
                st.dataframe(df.head())  # Show the first 5 rows

                # Convert to CSV
                csv = df.to_csv(index=False).encode("latin-1")
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name="converted.csv",
                    mime="text/csv"
                )

            elif option == "CSV to Parquet":
                # Read the CSV file into a pandas Dataframe

                df = pd.read_csv(loaded_file, sep=option_2, encoding="latin-1")

                # Show a basic preview of the file
                st.write("Preview")
                st.dataframe(df.head())  # Show the first 5 rows

                # Convert to Parquet
                parquet = io.BytesIO()
                df.to_parquet(parquet, index=False)
                st.download_button(
                    label="Download Parquet",
                    data=parquet.getvalue(),
                    file_name="converted.parquet",
                    mime="application/octet-stream"
                )

        except Exception as e:
            st.error(f"An error occurred while trying to convert the file: {e}")
    else:
        st.warning(f"Please, load a {option.split()[0]} file.")

if __name__ == "__main__":
    main()