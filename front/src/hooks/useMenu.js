import { ref, computed } from "vue";

export function useMenu() {
  const menuVisible = ref(false);

  const handleMenu = () => (menuVisible.value = !menuVisible.value);

  const closeModal = () => (menuVisible.value = false);

  const handleMenuClass = computed(() => {
    return menuVisible.value ? "catalog_cart" : "catalog_cart_hidden";
  });

  return {
    menuVisible,
    handleMenu,
    closeModal,
    handleMenuClass,
  };
}
