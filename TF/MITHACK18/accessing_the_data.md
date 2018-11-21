# Accessing the data

The easiest way to access the data is via the uncharted/s3-proxy docker image. Docker provides an simple way to package all the libraries and dependencies you need to run an application. *Get set up with docker here[https://docs.docker.com/get-started/]*

For our purposes, the uncharted/s3-proxy docker image will allow you to download the data, and also provide a convenient mechanism for serving out images to a web browser. 

**After you have Docker up and running: **

1. Create a file named `.env` that contains the following:
```bash
SERVER_LISTEN_PORT=3000
AWS_DEFAULT_BUCKET=hack-for-freedom
AWS_DEFAULT_REGION=us-gov-west-1
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
```
Where your access and secret keys are filled in.  **Please do not share your keys with anyone!**

2. Start the proxy container by entering the following into the terminal:
```bash
docker run --env-file ./.env -p 3000:3000 uncharted/s3-proxy
```

3. In the dropbox, you'll find the `download_tellfinder_data.sh` file to download all of the raw data. Enter the following prompt into the terminal: 
```bash
./download_tellfinder_data.sh
```

# Serving Images

The uncharted/s3-proxy docker image also provides a mechanism to serve out images to a web browser.  For example, consider the following TellFinder document:
```json
{
  "id": "ad::2FB74A68422AD1BDEFCC356DD71141846B0D60C10D0220405A52AA06ECFAD9F8",
  "title": "(520) 487-5278 - San Fernando Valley Escorts - CityXGuide",
  "body": "Contact: (520) 487-5278",
  "type": "Document",
  "subtype": "Ad",
  "feature": {
    "image_sha1_logo": [
      "C1FC6009C3A3D6C9EC5BD6CADD86AB2A77A8A153"
    ],
    "image_sha1_photo": [
      "E3086D96091E355DEA8032546AA10AE5E2B6A2EA",
      "7F4ED1A990B08EF5CD5EF8E52AB834FC1531AFEB",
      "85096D81B9798199E214CF11CF57D90413EB6EA6",
      "482F8EDCD5F3A440D6E0A9D0C70E2A5F18F04D4E"
    ]
    "image_sha1": [
      "E3086D96091E355DEA8032546AA10AE5E2B6A2EA",
      "7F4ED1A990B08EF5CD5EF8E52AB834FC1531AFEB",
      "85096D81B9798199E214CF11CF57D90413EB6EA6",
      "C1FC6009C3A3D6C9EC5BD6CADD86AB2A77A8A153",
      "482F8EDCD5F3A440D6E0A9D0C70E2A5F18F04D4E"
    ]
    ...
}
```
The images may be accessed as follows:
```html
	<img src="http://localhost:3000/images/C1FC6009C3A3D6C9EC5BD6CADD86AB2A77A8A153">
```

#  Data Dictionary	

You are doing great! Now, lets talk about the data. 

You'll be working with 5 months of structured content served within TellFinder and used by law enforcement everyday. 

From February 2018 - May 2018, this repository swells to approximately 9 million documents and 1 million images. The table below provides descriptions and key-values from the extractions for more context.

| key-value                 | key               | description                                                  | example                                                      |
| ------------------------- | ----------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| body                      | Body              | All text found within the collected document.                | Welcome, 555-111-1212, Hello There, mary@example.com         |
| title                     | Title             | The title of the document.                                   | The New York Times, Most popular stories - Forbes            |
| feature.email             | Email             | An email address found within a document.                    | mary@example.com, mary@example.*, *@specificdomain.com       |
| feature.username          | Username          | A username (eg from a web forum, etc)                        | JohnDoe_1975                                                 |
| feature.phone             | Phone             | A phone number found within an document.                     | (555)111-1212, 555-111-1212, 5551111212, etc                 |
| feature.website           | Website           | An external link found within a document.                    | http://link-to-my-personal-website.com                       |
| locality.label            | Location          | A specific location (usually a city) found within the document. Used to plot locations on a map. | Toronto, ON, Canada                                          |
| locality.dateBegin        | Post Time         | The time at which the document was posted.                   | 2017-12-31 (match an exact day), [2016-12-31,] (matches from December 31st, 2016 until today), [2016-12-1,2016-12-31] (matches the month of December 2016) |
| subtype                   | Type              | The type of document to search over.                         | Ad, Post, etc                                                |
| feature.name              | Name              | A persons name found within the document.                    | david, mya, fiona                                            |
| feature.organization_name | Organization Name | An organization name found within the document.              | Joes Plumbing Service, The New York Yankees                  |