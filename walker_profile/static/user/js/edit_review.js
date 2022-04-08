const openEditModal = document.querySelector("#open-edit-modal");
const closeEditModal = document.querySelector(".close-delete-btn");
// / Function opens Prices Modal
function showEditModal() {
  let showDeleteModal = document.querySelector(".delete-rev-wrapper");
  showDeleteModal.classList.toggle("show-modal");
}

openEditModal.addEventListener("click", showEditModal);
closeEditModal.addEventListener("click", showEditModal);
