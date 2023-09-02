// document.addEventListener("DOMContentLoaded", function() {
//     const editOption = document.querySelector(".edit-option");
//     const postContent = document.querySelector(".post-content");
//     const editContent = document.createElement("textarea");
//     editContent.classList.add("edit-content");
//     editContent.value = postContent.textContent;

//     editOption.addEventListener("click", function(event) {
//         event.preventDefault();
//         postContent.style.display = "none";
//         postContent.parentElement.appendChild(editContent);
//         editContent.focus();
//         editContent.style.display = "block";

//         const confirmEditButton = document.createElement("button");
//         confirmEditButton.textContent = "Confirm Edit";
//         confirmEditButton.classList.add("confirm-edit-button");

//         postContent.parentElement.appendChild(confirmEditButton);

//         confirmEditButton.addEventListener("click", function() {
//             const editedContent = editContent.value;
//             // Use the 'edit_post' URL to send the edited content to the server
//             window.location.href = `/edit_post/${post_id}/?content=${encodeURIComponent(editedContent)}`;
//         });
//     });
// });
// function confirmDelete(postId) {
//     const confirmed = confirm("Are you sure you want to delete this post?");
//     if (confirmed) {
//         window.location.href = `/polls/delete_post/${postId}/`;
//     }
// }

