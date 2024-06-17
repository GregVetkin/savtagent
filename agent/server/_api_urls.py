"""
Файл служит для хранения маршрутов API сервера.
Изменения маршрутов, как и добавление, производить только в этом файле.
"""
# CPU
# ===============================================================================
API_CPU_USAGE                   = "/cpu/usage"
# ===============================================================================
# File
# ===============================================================================
API_FILE_INFO                   = "/file/info"
API_FILE_REGEX                  = "/file/regex"
# ===============================================================================
# Memory
# ===============================================================================
API_MEMORY                      = "/memory"
API_MEMORY_RAM                  = "/memory/ram"
API_MEMORY_SWAP                 = "/memory/swap"
# ===============================================================================
# Network
# ===============================================================================
API_NETWORK_CONNECTIONS         = "/network/connections"
API_NETWORK_INTERFACE           = "/network/interface"
API_NETWORK_INTERFACE_CONCRETE  = "/network/interface/<string:interface_name>"
API_NETWORK_COLLISIONS          = "/network/collisions"
# ===============================================================================
# Processes
# ===============================================================================
API_PROCESS                     = "/process"
API_PROCESS_CONCRETE            = "/process/<int:pid>"
# ===============================================================================
# Storage
# ===============================================================================
API_STORAGE                     = "/storage"
# ===============================================================================
# System
# ===============================================================================
API_SYSTEM_LOGS                 = "/system/logs"
API_SYSTEM_SHUTDOWN             = "/system/shutdown"
API_SYSTEM_REBOOT               = "/system/reboot"
API_SYSTEM_NOTIFICATION         = "/system/notification"
API_SYSTEM_ACTIVE_USERS         = "/system/users/active"
API_SYSTEM_TIME                 = "/system/time"
API_SYSTEM_UPTIME               = "/system/uptime"
# ===============================================================================