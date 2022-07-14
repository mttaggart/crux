console.log("I'M ALIIIIVE");

function getTab() {
    return new Promise((resolve, reject) => {
        chrome.tabs.query({active: true, currentWindow: true}, tabs => {
            const tab = tabs[0];
            resolve(tab);
        });
    });
}

async function doAThing() {
    const tab = await getTab();
    chrome.scripting.executeScript({
        target: {tabId: tab.id},
        files: ["contentscript.js"]
    },
    () => {alert(";)");})
}


document.getElementById("demo-button")
.addEventListener("click", () => {
    doAThing();
})