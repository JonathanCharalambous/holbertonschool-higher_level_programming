document.querySelector("#add_item").addEventListener("click", addItem);

function addItem() {
    const newItem = document.createElement("li");
    newItem.textContent = "Item";
    document.querySelector("ul.my_list").appendChild(newItem);
}