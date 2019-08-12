function drag(ev) {
      ev.dataTransfer.setData("text", ev.target.id);
      event.preventDefault()
    }
