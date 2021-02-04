window.addEventListener("load", onLoad);
// wird aufgerufen, wenn das plugin angeklickt wird - on load of plugin
async function onLoad() {
    window.document.getElementById("trainmodel").addEventListener("click",trainModel);
    window.document.getElementById("predict").addEventListener("click",sendContentMail);
    browser.runtime.onMessage.addListener(handleMessageBackground);
    }

async function sendContentMail(){
    //html element änderung durch veränderung des texts für eine anzeige,
    //dass der text verarbeitet wird und die auswahl bereits getroffen wurde
    document.getElementById("start").innerHTML = "";
    document.getElementById("processing").innerHTML = "Your email is being processed...";
    //zugriff auf die email
    const tabs = await browser.tabs.query({
        active: true,
        currentWindow: true,
        })
    const tabId = tabs[0].id;
    const message = await browser.messageDisplay.getDisplayedMessage(tabId);
    console.log(message)
    const messageraw = await browser.messages.getFull(message.id);
    //der ordner der zurückgegeben wurde wird durch iterateMail zu
    //plain text verarbeitet und in der variable gespeichert
    var email = iterateMail(messageraw);
    var emailjson = {
        email:email[0],
        type:email[1]
        };

    var sending = browser.runtime.sendMessage({
        process : "sendContent",
        emailText: emailjson.email,
        type: emailjson.type
        });
    };

async function reply(){
    var sending = browser.runtime.sendMessage({
        process : "reply",
        emailContent : document.getElementById("email-content").innerHTML
      });
    }
async function replyAll(){
    var sending = browser.runtime.sendMessage({
        process : "replyAll",
        emailContent : document.getElementById("email-content").innerHTML
        });
    }
async function trainModel(){
    var inboxMessages = await messenger.accounts.list();
    var accountid = inboxMessages[0].folders[0]
    //console.log(accountid)
    var emails =  await browser.messages.list(accountid)
    //console.log(emails.messages)
    for (var i = 0; i < emails.messages.length; i++) {
        //console.log(emails.messages[i].id)
        message = await browser.messages.getFull(emails.messages[i].id);
        var sending = browser.runtime.sendMessage({
            process : "trainModel",
            emailText : iterateMail(message)[0]
            });
        }
    }
function handleMessageBackground(request) {
    console.log("Message from the content script: " +
      request.process);
      if (request.process == "generatedEmail"){
        document.getElementById("processing").innerHTML = "";  
        document.getElementById("email-content").innerHTML = request.email;
        document.getElementById("header-email").innerHTML = "Your response:";
        window.document.getElementById("reply").addEventListener("click",reply);
        window.document.getElementById("replyAll").addEventListener("click",replyAll);    
      }else if(request.process == "Error"){
        document.getElementById("email-content").innerHTML = request.message;
      }
      }


function iterateMail(message){
    var finalmessage = "";
    for (i = 0; i < message.parts.length; i++) {
        if(message.parts[i].contentType == "text/html"){
            finalmessage = message.parts[i];
            console.log("HTML");
        }
        else if( message.parts[i].contentType == "text/plain"){
            finalmessage = message.parts[i];
            break;
        }
        else{
            return iterateMail(message.parts[i]);
        }
    }
    return [finalmessage.body, finalmessage.contentType];
    }