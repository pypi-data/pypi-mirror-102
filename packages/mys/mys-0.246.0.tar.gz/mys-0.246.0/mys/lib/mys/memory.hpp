#pragma once

#include <memory>
#include <cstdlib>
#include <algorithm>

namespace mys {

// A shared pointer class for single threaded applications made
// specifically for Mys.
template<class T>
class shared_ptr final
{
public:
    void *m_buf_p;

    shared_ptr(void) noexcept
        : m_buf_p(nullptr)
    {
    }

    // Shared from this.
    shared_ptr(T *ptr) noexcept
    {
        m_buf_p = (((int *)ptr) - 1);
        count() += 1;
    }

    shared_ptr(std::nullptr_t) noexcept
        : m_buf_p(nullptr)
    {
    }

    shared_ptr(const shared_ptr<T> &other) noexcept
        : m_buf_p(other.m_buf_p)
    {
        if (m_buf_p != nullptr) {
            count() += 1;
        }
    }

    template<class U>
    shared_ptr(const shared_ptr<U>& ptr) noexcept
        : m_buf_p(ptr.m_buf_p)
    {
        count() += 1;
    }

    ~shared_ptr()
    {
        if (m_buf_p != nullptr) {
            decrement();
        }
    }

    void decrement()
    {
        count() -= 1;

        if (count() == 0) {
            std::destroy_at(get());
            std::free(m_buf_p);
        }
    }

    int& count() const noexcept
    {
        return *(int *)m_buf_p;
    }

    T *get() const noexcept
    {
        return (T *)(((int *)m_buf_p) + 1);
    }

    T *operator->() const noexcept
    {
        return get();
    }

    T& operator*() const noexcept
    {
        return *get();
    }

    shared_ptr& operator=(shared_ptr other) noexcept
    {
        std::swap(m_buf_p, other.m_buf_p);

        return *this;
    }

    shared_ptr& operator=(std::nullptr_t)
    {
        if (m_buf_p != nullptr) {
            decrement();
            m_buf_p = nullptr;
        }

        return *this;
    }

    operator bool() const
    {
        return m_buf_p != nullptr;
    }

    int use_count(void) const
    {
        if (m_buf_p == nullptr) {
            return 0;
        } else {
            return count();
        }
    }
};

template<class T, class... Args>
shared_ptr<T> make_shared(Args&&... args)
{
    shared_ptr<T> p;

    p.m_buf_p = std::malloc(sizeof(int) + sizeof(T));

    if (p.m_buf_p == nullptr) {
        throw std::bad_alloc();
    }

    p.count() = 1;

    try {
        new(p.get()) T(std::forward<Args>(args)...);
    } catch (...) {
        std::free(p.m_buf_p);
        p.m_buf_p = nullptr;

        throw;
    }

    return p;
}

template<class T, class U>
shared_ptr<T> dynamic_pointer_cast(const shared_ptr<U>& ptr)
{
    if (ptr.m_buf_p != nullptr) {
        T *casted = dynamic_cast<T *>(ptr.get());

        if (casted != nullptr) {
            return shared_ptr<T>(casted);
        } else {
            return shared_ptr<T>();
        }
    } else {
        return shared_ptr<T>();
    }
}

}
