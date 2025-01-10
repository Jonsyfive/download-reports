import os
import requests


def download(url, file_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):  # Read in chunks
                if chunk:  # Filter out keep-alive chunks
                    f.write(chunk)
    else:
        print(
            f"Failed to download the File. Status code: {response.status_code}: {url}"
        )


with open("company_data.csv", "r") as f:
    data = f.read()
    print(type(data))

company_list = data.split("\n")[1:]
print(company_list)
company_dict = {}
for company in company_list:
    company_data = company.split(",")
    company_name = company_data[0]
    company_dict[company_name] = company_data[1:]

# print(company_dict)

# create folder for each company
for company in company_dict.keys():
    # print(company)
    os.makedirs("companies/" + company, exist_ok=True)
    # create subfolders

    if company_dict[company][1] != "":
        os.makedirs("companies/" + company + "/pdf_DE", exist_ok=True)
        download(
            company_dict[company][1], f"companies/{company}/pdf_DE/{company}_DE.pdf"
        )
    if company_dict[company][2] != "":
        os.makedirs("companies/" + company + "/pdf_EN", exist_ok=True)

        download(
            company_dict[company][2], f"companies/{company}/pdf_EN/{company}_EN.pdf"
        )
    if company_dict[company][3] != "":
        os.makedirs("companies/" + company + "/zip_DE", exist_ok=True)
        download(company_dict[company][3], f"companies/{company}/zip_DE/{company}.zip")
    if company_dict[company][4] != "":
        os.makedirs("companies/" + company + "/zip_EN", exist_ok=True)
        download(company_dict[company][4], f"companies/{company}/zip_EN/{company}.zip")
    if company_dict[company][5] != "":
        os.makedirs("companies/" + company + "/esg", exist_ok=True)
        download(company_dict[company][5], f"companies/{company}/esg/{company}.pdf")
    if company_dict[company][6] != "":
        os.makedirs("companies/" + company + "/esg_en", exist_ok=True)
        download(company_dict[company][6], f"companies/{company}/esg_en/{company}.pdf")
