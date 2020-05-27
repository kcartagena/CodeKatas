export function sortKatas() {
    let list, x, switching, b, shouldSwitch;

    list = document.querySelector("ul");
      switching = true;

/* Make a loop that will continue until no switching has been done: */
  while (switching) {
    // 1. Assume no switching is done:
    switching = false;
    b = list.querySelector("li");

    // 2. Loop through all list-items:
    for (x = 0; x < (b.length - 1); x++) {
      // start by saying there should be no switching:
      shouldSwitch = false;
      /* check if the next item should
      switch place with the current item: */
      if (b[x].innerHTML.toLowerCase() > b[x + 1].innerHTML.toLowerCase()) {
        /* if next item is alphabetically
        lower than current item, mark as a switch
        and break the loop: */
        shouldSwitch = true;
        break;
      }
    }
    if (shouldSwitch) {
      /* If a switch has been marked, make the switch
      and mark the switch as done: */
      b[x].parentNode.insertBefore(b[x + 1], b[x]);
      switching = true;
    }
  }
}

sortKatas();
