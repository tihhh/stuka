function deleteNote(noteId) {
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({ noteId: noteId }),
        headers: {
            "Content-Type": "application/json"
        }
    }).then((_res) => {
        window.location.href = "/";
    });
}

function createThread() {
    window.location.href = "/chat"
}