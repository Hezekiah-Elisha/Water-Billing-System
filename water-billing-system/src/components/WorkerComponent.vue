<template>
    <div class="modal container-fluid card" @click.self="$emit('close')">
      <div class="modal-content" @click.stop>
        <span class="close" @click="$emit('close')">&times;</span>
        <slot></slot>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'CustomWorkerModal',
  };
  </script>
  
  <style scoped>
  .modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.7);
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  
  .modal-content {
    background-color: #fff;
    padding: 20px;
    width: 50%;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    position: relative;
  }
  
  .close {
    position: absolute;
    top: 10px;
    right: 10px;
    font-size: 24px;
    font-weight: bold;
    cursor: pointer;
    padding: 5px 10px;
    background-color: var(--primary-color);
    color: white;
    border-radius: 10px;
  }
  .close:hover {
    background-color: var(--secondary-color);
  }
  
  </style>